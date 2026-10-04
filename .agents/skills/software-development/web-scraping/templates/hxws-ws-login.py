#!/usr/bin/env python3
"""
hxws WebSocket Binary Login Template

Reusable Python implementation for connecting to hxws-based binary WebSocket
protocols (used by Chinese gaming/casino platforms). This template handles:

1. Binary frame construction matching the Ku class encoding
2. MD5 password hashing
3. Account string formatting: {tag}00{callingCode}{phone}
4. UTF-16LE fixed-length string encoding with zero-padding
5. UTF-8 variable-length string encoding

Usage:
    python hxws_login.py

Requirements:
    pip install websockets

Protocol constants and field schemas must be extracted from the target site's
JS bundle before using this template. See the web-scraping skill's
references/hxws-websocket-binary-protocol.md for the reverse-engineering guide.

To customize for a new target:
    1. Update WS_URL to the target's WebSocket endpoint
    2. Update MDM/SUB command constants from the JS bundle
    3. Adjust field schemas to match the target's packet structure
    4. Set the correct calling_code, phone, and password
    5. Adjust machine_id generation if needed
"""

import asyncio
import hashlib
import random
import socket
import struct
import time
import uuid

import websockets

# ============================================================
# CONFIGURATION — customize per target
# ============================================================

WS_URL = "wss://wsoro7777.spiritapis.com/net"

# Protocol constants (extract from JS bundle)
MDM_MB_LOGON = 1
SUB_MB_LOGON_ACCOUNTS = 2
SUB_MB_LOGON_SUCCESS = 100
SUB_MB_LOGON_FAILURE = 101

# Credentials (from form or config)
PHONE = "3015347365"
PASSWORD = "lol123213aS123"
CALLING_CODE = "57"  # Colombia
TAG = ""  # From skin config tags[hostname]


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def md5hex(s: str) -> str:
    """MD5 hash as lowercase hex string (32 chars)."""
    return hashlib.md5(s.encode()).hexdigest()


def generate_machine_id() -> str:
    """Generate a 32-char hex machine ID like the browser fingerprint."""
    seed = f"{random.getrandbits(128)}{time.time()}{uuid.uuid4()}"
    return md5hex(seed)[:32]


def get_local_ip_bytes() -> bytes:
    """Get local IPv4 as 4 bytes for the ipAddr field."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return bytes(int(x) for x in ip.split("."))
    except Exception:
        return bytes([127, 0, 0, 1])


# ============================================================
# KU BINARY WRITER (matches JS Ku class)
# ============================================================

class KuWriter:
    """
    Binary packet writer matching the JS Ku class in hxws-based platforms.
    
    Frame format sent over WebSocket:
        [mainCmd LE][subCmd LE][encoded payload fields...]
    """
    
    def __init__(self, main_cmd: int, sub_cmd: int):
        self.main_cmd = main_cmd
        self.sub_cmd = sub_cmd
        self.buf = bytearray()
    
    def u8(self, v: int):
        self.buf += struct.pack("<B", v & 0xFF)
    
    def u16(self, v: int):
        self.buf += struct.pack("<H", v & 0xFFFF)
    
    def u32(self, v: int):
        self.buf += struct.pack("<I", v & 0xFFFFFFFF)
    
    def i64(self, v: int):
        self.buf += struct.pack("<q", v)
    
    def pad(self, n: int):
        if n > 0:
            self.buf += b"\x00" * n
    
    def write_utf16(self, text: str, fixed_len: int = 0):
        """
        Write UTF-16LE string matching JS Ku.writeUTF16().
        
        If fixed_len > 0: write up to fixed_len-1 chars, zero-pad
        remaining char positions, then null terminator.
        If fixed_len == 0: variable length, just chars + null.
        
        Each char16_t is 2 bytes. Total byte size = fixed_len * 2.
        
        The null terminator is ALWAYS written after the content,
        even for fixed-length fields. This matches the C++ behavior.
        """
        if fixed_len == 0:
            for ch in text:
                self.u16(ord(ch))
            self.u16(0)  # null terminator
        else:
            max_chars = fixed_len - 1
            chars_written = min(len(text), max_chars)
            for ch in text[:chars_written]:
                self.u16(ord(ch))
            # Zero-pad remaining char positions (excluding null)
            self.pad((max_chars - chars_written) * 2)
            self.u16(0)  # null terminator
    
    def write_utf8(self, text: str, fixed_len: int = 0):
        """
        Write UTF-8 string matching JS Ku.writeUTF8().
        
        If fixed_len > 0: write up to fixed_len-1 bytes, zero-pad,
        then null terminator.
        If fixed_len == 0: variable length, just bytes + null.
        """
        encoded = text.encode("utf-8")
        if fixed_len == 0:
            self.buf += encoded
            self.buf += b"\x00"
        else:
            max_bytes = fixed_len - 1
            bytes_written = min(len(encoded), max_bytes)
            self.buf += encoded[:bytes_written]
            self.pad(max_bytes - bytes_written)
            self.buf += b"\x00"
    
    def get_frame(self) -> bytes:
        """Build the full WebSocket binary frame: header + payload."""
        header = struct.pack("<HH", self.main_cmd, self.sub_cmd)
        return header + bytes(self.buf)


# ============================================================
# LOGIN PACKET BUILDER (customize per target schema)
# ============================================================

def build_login_packet(
    phone: str = PHONE,
    password: str = PASSWORD,
    calling_code: str = CALLING_CODE,
    tag: str = TAG,
    machine_id: str = None,
) -> bytes:
    """Build the SUB_MB_LOGON_ACCOUNTS binary packet."""
    if machine_id is None:
        machine_id = generate_machine_id()
    
    accounts = f"{tag}00{calling_code}{phone}"
    pw_hash = md5hex(password)
    ip_bytes = get_local_ip_bytes()
    
    k = KuWriter(MDM_MB_LOGON, SUB_MB_LOGON_ACCOUNTS)
    
    k.u16(0)                    # moduleID
    k.u32(0)                    # plazaVersion
    k.u8(2)                     # deviceType (2=web)
    k.write_utf16(machine_id, 33)  # machineID[33]
    k.write_utf16(accounts, 32)    # accounts[32]
    k.write_utf16(pw_hash, 33)     # logonPass[33]
    
    # ipAddr: uint8_t[14] — 14 zero bytes
    k.buf += ip_bytes[:4]
    k.pad(10)
    
    k.write_utf8("H5", 0)          # channelName (variable)
    k.u32(0)                       # spreadBindID
    
    return k.get_frame()


# ============================================================
# RESPONSE PARSER
# ============================================================

def parse_response(data: bytes) -> dict:
    """Parse the binary response frame."""
    if len(data) < 4:
        return {"error": "too short"}
    
    main_cmd, sub_cmd = struct.unpack_from("<HH", data, 0)
    result = {"mainCmd": main_cmd, "subCmd": sub_cmd}
    
    if sub_cmd == SUB_MB_LOGON_SUCCESS:
        result["status"] = "success"
        if len(data) >= 6:
            result["faceID"] = struct.unpack_from("<H", data, 4)[0]
        if len(data) >= 8:
            result["userID"] = struct.unpack_from("<I", data, 8)[0]
            
    elif sub_cmd == SUB_MB_LOGON_FAILURE:
        result["status"] = "failure"
        if len(data) >= 8:
            result["errorCode"] = struct.unpack_from("<I", data, 4)[0]
    
    return result


# ============================================================
# MAIN LOGIN FUNCTION
# ============================================================

async def login(max_wait: int = 15) -> dict:
    """Connect to WebSocket, send login packet, wait for response."""
    frame = build_login_packet()
    
    print(f"[*] Connecting to {WS_URL}")
    print(f"[*] Frame size: {len(frame)} bytes")
    print(f"[*] Accounts: 00{CALLING_CODE}{PHONE}")
    print(f"[*] MD5(pass): {md5hex(PASSWORD)}")
    
    try:
        async with websockets.connect(
            WS_URL,
            subprotocols=["binary"],
            ping_interval=30,
            ping_timeout=10,
            max_size=20 * 1024 * 1024,
            origin="https://kkbrio.love",  # Match the target
        ) as ws:
            print("[+] Connected")
            
            # Check for server init message
            try:
                msg = await asyncio.wait_for(ws.recv(), timeout=2.0)
                print(f"[*] Server init: {msg.hex()[:80]}")
            except asyncio.TimeoutError:
                pass
            
            # Send login
            await ws.send(frame)
            print("[+] Sent login packet")
            
            # Wait for response
            resp = await asyncio.wait_for(ws.recv(), timeout=max_wait)
            print(f"[+] Response: {len(resp)} bytes")
            
            result = parse_response(resp)
            print(f"[+] Status: {result.get('status', 'unknown')}")
            
            if result.get("status") == "success":
                print(f"    UserID: {result.get('userID')}")
            elif result.get("status") == "failure":
                print(f"    Error: {result.get('errorCode')}")
            
            return result
    
    except asyncio.TimeoutError:
        print("[-] Timeout - no response")
        return {"status": "timeout"}
    except websockets.exceptions.WebSocketException as e:
        print(f"[-] WS error: {e}")
        return {"status": "error", "error": str(e)}


if __name__ == "__main__":
    asyncio.run(login())
