# HXWS WebSocket Binary Protocol Analysis

## Source

Reverse-engineered from `kkbrio.love` (white-label casino using "oro7777" skin). The site uses Nuxt.js (Vue 3 SSR) with a custom binary WebSocket protocol for ALL server communication — no REST API for auth or game data.

## Architecture

```
Browser → WebSocket (wss://wsoro7777.spiritapis.com/net)
        → hxws library (hxws-1.1.1.0.js + hxws-1.1.1.0.wasm)
        → Binary packet encoding via C++ WASM Module
```

The `hxws` library is compiled from C++ via Emscripten. Source path found in WASM: `/mnt/d/MyProg/hxclient-webasm-network/HxWasmClientWebsocket/src/hxwebsocket.cpp`

## Command Structure

### Main Commands (MDM)

Found in the main JS bundle (`diLS-A9T.js`):

```
MDM_MB_LOGON: 1     # Login/authentication
```

### Sub-Commands (SUB) for MDM_MB_LOGON

```javascript
// Standard commands (used by most skins)
SUB_MB_LOGON_ACCOUNTS:        2    # Standard login with accounts
SUB_MB_REGISTER_ACCOUNTS:     3    # Register new account
SUB_MB_LOGON_OTHERPLATFORM:   4    # Social/OAuth login
SUB_MB_LOGON_VISITOR:         5    # Guest login
SUB_MB_LOGON_MOBILE_EX:       7    # Mobile-specific login
SUB_MB_RELOGON:              10    # Re-authentication
SUB_MB_LOGON_EXIT:           11    # Logout
SUB_MB_LOGON_EXIT_RESULT:    12    # Logout result
SUB_GP_SERVER_UTC_TIMESTAMP: 25    # Server time sync
SUB_GP_SERVER_UTC_TIMESTAMP_RESULT: 26
SUB_MB_LOGON_SUCCESS:       100    # Login success response
SUB_MB_LOGON_FAILURE:       101    # Login failure response
SUB_MB_REGISTER_FAILURE:    102    # Registration failure
SUB_MB_REGISTER_SUCCESS:    103    # Registration success
SUB_CLNT_NEED_LOGIN:        105    # Server requests re-login
SUB_MB_GetScoreInfo:        110    # User balance/score query
SUB_MB_SendSMSLogonCode:    120    # Send SMS login code
SUB_MB_SendSMSLogonCodeResult:    121
SUB_MB_SendSMSResetPassword:      122
SUB_MB_SendSMSResetPasswordResult: 123
SUB_MB_SendSMSRegisteUser:        124
SUB_MB_SendSMSRegisteUserResult:  125
SUB_MB_RESET_LOGON_PASSWORD:      130
SUB_MB_RESET_LOGON_PASSWORD_RESULT: 131

// V6 variants (some newer servers use these instead)
SUB_MB_LOGON_ACCOUNTS_V6:      602
SUB_MB_REGISTER_ACCOUNTS_V6:   603
SUB_MB_LOGON_OTHERPLATFORM_V6: 604
SUB_MB_LOGON_VISITOR_V6:       605
SUB_MB_LOGON_MOBILE_EX_V6:     607
SUB_MB_RELOGON_V6:             610
```

## Packet Structure Schemas

### SUB_MB_LOGON_ACCOUNTS (Request — V1, subCmd=2)

```javascript
// From the JS bundle schema definition:
{
    t: "uint16_t",  k: "moduleID"
    t: "uint32_t",  k: "plazaVersion"
    t: "uint8_t",   k: "deviceType"
    t: "char16_t",  k: "machineID",   s: LEN_MACHINE_ID    // 33
    t: "char16_t",  k: "accounts",    s: LEN_ACCOUNTS      // 32
    t: "char16_t",  k: "logonPass",   s: LEN_MD5           // 33
    t: "uint8_t",   k: "ipAddr",      s: 14
    t: "utf8",      k: "channelName", s: 0                 // variable
    t: "uint32_t",  k: "spreadBindID"
}
```

### SUB_MB_LOGON_ACCOUNTS_V6 (Request — V6, subCmd=602)

```javascript
{
    ...same V1 fields up to logonPass...
    t: "utf8",      k: "clientIP",    s: LEN_IP_V6         // 48 chars
    t: "utf8",      k: "channelName", s: 1024              // fixed 1024 bytes
}
```

Key differences in V6:
- `clientIP` is utf8[48] instead of uint8_t[14]
- `channelName` is utf8[1024] (fixed) instead of utf8 variable
- The V6 subCmd values start at 600+ (602 vs 2)

### SUB_MB_LOGON_SUCCESS (Response — both versions)

```javascript
{
    t: "uint16_t",  k: "faceID"
    t: "uint8_t",   k: "gender"
    t: "uint32_t",  k: "customID"
    t: "uint32_t",  k: "userID"
    t: "uint32_t",  k: "gameID"
    t: "uint32_t",  k: "experience"
    t: "int64_t",   k: "loveLiness"
    t: "char16_t",  k: "accounts",    s: 32
    t: "char16_t",  k: "nickName",    s: 32
    t: "char16_t",  k: "dynamicPass", s: 33
    t: "int64_t",   k: "userScore"
    t: "int64_t",   k: "tCCoin"
    t: "int64_t",   k: "userInsure"
    t: "int64_t",   k: "tCCoinInsure"
    t: "uint8_t",   k: "insureEnabled"
    t: "uint8_t",   k: "isAgent"
    t: "uint8_t",   k: "moorMachine"
    t: "int64_t",   k: "roomCard"
    t: "uint32_t",  k: "lockServerID"
    t: "uint32_t",  k: "kindID"
    t: "uint32_t",  k: "agentID"
    t: "uint32_t",  k: "userFlag"
}
```

### SUB_MB_GetScoreInfo (Response)

```javascript
{
    t: "int64_t",   k: "score"          // Main balance
    t: "int64_t",   k: "insureScore"    // Insured balance
    t: "int64_t",   k: "cCoin"          // Bonus/coin balance
    t: "int64_t",   k: "cCoinInsure"    // Insured bonus coins
    t: "uint8_t",   k: "growLevel"      // VIP/level
    ...
}
```

### SUB_MB_LOGON_FAILURE (Response)

```javascript
{
    t: "int32_t",   k: "errorCode"
}
```

## Ku Binary Writer Class (JavaScript Implementation)

The Ku class in the main JS bundle handles binary encoding:

```javascript
class Ku {
    constructor(mainCmd, subCmd) {
        this.ws = Module.WebsocketClient.instance();
        const bufSize = this.ws.getSendBufferSize();
        // allocSendBuffer writes [mainCmd(LE)][subCmd(LE)] header + returns payload pointer
        const ptr = this.ws.allocSendBuffer(mainCmd, subCmd, 0);
        this.dataView = new DataView(Module.HEAPU8.buffer, ptr, bufSize);
        this.offset = 0;
    }
    writeUint8(v)   { this.dataView.setUint8(this.offset++, v) }
    writeUint16(v)  { this.dataView.setUint16(this.offset, v, true); this.offset += 2 }
    writeUint32(v)  { this.dataView.setUint32(this.offset, v, true); this.offset += 4 }
    writeInt64(v)   { this.dataView.setBigInt64(this.offset, BigInt(v), true); this.offset += 8 }
    
    // UTF-16 with fixed-length padding (s > 0): write up to s-1 chars, zero-pad, then null
    // UTF-16 with variable length (s = 0): write chars, then null
    writeUTF16(str, fixedLen) {
        if (fixedLen === 0) {
            for (let i = 0; i < str.length; i++) this.writeUint16(str.charCodeAt(i));
        } else {
            for (let i = 0, max = Math.min(str.length, fixedLen - 1); i < max; i++)
                this.writeUint16(str.charCodeAt(i));
            this.padding(0, (fixedLen - 1 - str.length) * 2);
        }
        this.writeUint16(0);  // null terminator
    }
    
    // UTF-8 with same logic (fixed padding vs variable)
    writeUTF8(str, fixedLen) {
        const enc = new TextEncoder().encode(str);
        // ... null-terminated, zero-padded to fixedLen bytes
    }
    
    padding(val, byteCount) {
        // Write val repeatedly for byteCount bytes
    }
    
    send() {
        return this.ws.sendNetData(this.offset);
    }
}
```

The raw WebSocket binary frame sent by `sendNetData()` is:
```
[header: mainCmd(LE)][header: subCmd(LE)][payload: Ku-encoded fields...]
```

The `allocSendBuffer(mainCmd, subCmd, 0)` C++ WASM function:
1. Allocates a send buffer from the WASM heap
2. Writes the 4-byte header (mainCmd + subCmd, both uint16 LE)
3. Returns the buffer pointer pointing to AFTER the header (where Ku writes)

**IMPORTANT LIMITATION**: The functions `allocSendBuffer`, `getSendBufferSize`, and `sendNetData` are C++ class methods on `WebsocketClient` registered via **embind** (Emscripten's C++/JS binding library) at WASM runtime. They are NOT direct WASM exports. Analysis of the WASM binary (136KB, 753 functions, 22 exports, 44 imports) using `wasmtime` confirmed:
- The only WASM exports are low-level: `malloc`, `free`, `htonl`, `htons`, `ntohs`, stack management, and emscripten initialization.
- The 44 imports include complex JS bridge functions (`_emval_call`, `_embind_register_class`, `emscripten_websocket_*`) from both `env` and `wasi_snapshot_preview1`.
- The embind registration happens at runtime when the WASM's `main()` executes in the browser context.
- This means: these functions **cannot be called from Python** without running the full hxws WASM environment with all emscripten/emval imports. A standalone WASM runtime (wasmtime/wasmer) is not feasible without reimplementing the entire Emscripten bridge.

### String Length Constants

```javascript
LEN_PASSWORD           = 33   // char16_t[33] = 66 bytes
LEN_IP                 = 16   // uint8_t[16] = 16 bytes
LEN_IP_V6              = 48   // utf8[48] = 48 bytes
LEN_MACHINE_ID         = 33   // char16_t[33] = 66 bytes (32 chars + null)
LEN_MD5                = 33   // char16_t[33] = 66 bytes (32 hex chars + null)
LEN_NICKNAME           = 32   // char16_t[32] = 64 bytes
LEN_ACCOUNTS           = 32   // char16_t[32] = 64 bytes
LEN_MOBILE_PHONE       = 12   // char16_t[12] = 24 bytes
LEN_INTERNATIONAL_MOBILE = 16  // char16_t[16] = 32 bytes
LEN_MOBILE_CHECKCODE   = 7    // char16_t[7] = 14 bytes
```

## Account Format

The accounts string is constructed as:

```javascript
const accounts = tag + "00" + callingCode + phoneNumber;

// Example: "" + "00" + "57" + "3015347365" = "00573015347365"
```

- `tag`: Platform-specific tag (from config's `tags` object keyed by hostname, or default empty string `""`)
- `00`: Fixed separator
- `callingCode`: Country code (57 for Colombia)
- `phoneNumber`: User's phone number

## Password Hashing

Passwords are **MD5 hashed** before being sent in the `logonPass` field.

```javascript
const logonPass = Mr.md5(password);  // lowercase 32-char hex string
```

The MD5 module is embedded inline in the main bundle (not using crypto.subtle).

## Device Type Enum

```javascript
{
    DESKTOP:     3,   // PC_H5
    ANDROID_APP: 17,  // Android native app
    ANDROID_H5:  19,  // Android web
    APPLE_H5:    51,  // iOS web
    DEFAULT:     34,  // Fallback
}
```

PWA flag adds +1 to the base value.

## Machine ID (Device Fingerprint)

```javascript
const fingerprint = `{timestamp}${userAgent}${userAgent}`;
const machineID = MD5(fingerprint).substring(0, 32);
```

Stored in localStorage as `newMacID`.

## IP Address Resolution

```javascript
try {
    await getExternalIP();  // Fetches public IP
    ip = storedIP || "127.0.0.1";
} catch {
    ip = "127.0.0.1";
}
```

## Complete Login Flow

```javascript
// 1. Get form fields
const { phoneNumber, password } = ruleForm;

// 2. Determine tag for account string
const tag = tags[hostname] || defaultTag;  // Empty string for kkbrio.love

// 3. Build account and hash password
const accounts = tag + "00" + callingCode + phone;  // "00573015347365"
const logonPass = MD5(password);

// 4. Get device info
const deviceType = getDeviceType();
const machineID = getMachineID() || "";
const ip = await getIP() || "127.0.0.1";

// 5. Build data object
const data = {
    moduleID: 0, plazaVersion: 0, deviceType: deviceType,
    machineID: machineID, accounts: accounts,
    logonPass: logonPass, ipAddr: [ip],  // Note: wrapped in array!
    channelName: "", spreadBindID: 0,
};

// 6. Send via WebSocket
send(MDM_MB_LOGON, SUB_MB_LOGON_ACCOUNTS, data);

// 7. Listen for response
on(MDM_MB_LOGON, [SUB_MB_LOGON_SUCCESS, SUB_MB_LOGON_FAILURE], callback);
```

## Storage Mechanism

The hxws-based platform does NOT use HTTP cookies for authentication. Session data is stored exclusively in **localStorage**:

```
hall_newMacID     = enc0:{CryptoJS AES encrypted}  # Device fingerprint (MD5)
hall_Language     = enc0:{CryptoJS AES encrypted}  # UI language
hall_errorCount   = enc0:{CryptoJS AES encrypted}  # Error counter
loginInfos        = JSON string                    # Phone + password (remember me)
w_l_s_r           = JSON string                    # User session/state
```

### CryptoJS Encrypted Data

Values starting with `enc0:` contain base64-encoded CryptoJS AES ciphertext. The base64 decodes to a payload starting with `Salted__` (hex: `U2FsdGVkX18`), which is the standard CryptoJS marker for OpenSSL-compatible salted encryption. This cannot be decrypted without the secret key.

### document.cookie

Always empty. The platform does not set any cookies on the client.

### Implications for session extraction

- Filesystem-level cookie extraction (scanning Chrome's Cookies SQLite DB) will find NOTHING for this site — there are no cookies.
- localStorage scanning (Chrome's LevelDB at `%LOCALAPPDATA%\Google\Chrome\User Data\Default\Local Storage\leveldb\`) is the correct approach.
- The encrypted values (enc0:) are not directly usable — the session is maintained by the WebSocket connection itself, not by stored tokens.
- To resume a session, you must re-authenticate via the WebSocket protocol — the localStorage values alone are insufficient.
- CDP remote debugging (`Runtime.evaluate` to read `window.localStorage`) captures the decrypted/plaintext values directly from the live browser context.

## REST API Endpoints (HTTP)

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/get_push_config` | GET | Push notification config |
| `/api/cpfservice_info` | GET | CPF/ID config |
| `/api/customer_info` | GET | Customer support channels |
| `/api/withdraw_info` | GET | Withdrawal config |
| `/api/visitor` | GET | Visitor tracking |
| `/api/report` | POST | Analytics/event reporting |
| `/api/gift_code` | POST | Redeem gift code (signed) |

### API Signing (signedPost)

```javascript
function signedPost(url, data, secret) {
    const timestamp = Date.now();
    const sorted = Object.keys(data).sort()
        .map(k => encodeURIComponent(k) + "=" + encodeURIComponent(data[k]))
        .join("&");
    const signature = MD5(timestamp + sorted + secret);
    // Sends x-timestamp, x-signature headers + body
}
// Static secret key used: "7f6e5d4c3b2a1f0e9d8c7b6a"
```

## Game Provider IDs

From `gameTab.tabs`:

| Type | Provider | Category |
|------|----------|----------|
| 1 | PG Soft | Slots |
| 2 | Tada | Slots + crash |
| 12 | PP | Slots |
| 15 | Hacksaw | Crash/Dice/Limbo |
| 16 | FC | Slots |
| 17 | CQ9 | Slots + arcade |
| 18 | JDB | Slots |
| 19 | WG | Slots |
| 20 | Spade | Slots |
| 21 | G759 | Slots |
| 22 | POPOK | Slots |
| 4 | In-house slots | Tiger Fortune, Rabbit Fortune variants |
| 5 | In-house specialty | Mines, Penalty, Roulette, Keno, Bola da Sorte |

Type 3/4/5 games are managed by the platform directly (not external providers)
and may have `show: false` in the game list config, making them hidden from the
UI but still launchable via WebSocket commands.

Game image URL: `https://{cdn}/source/public/images/games/square/{size}/{gameId}.webp?t={version}`

## Additional Service Commands

Under `MDM_GP_USER_SERVICE`:
- Payment: `SUB_MB_GetProductInfos`, `SUB_MB_PlacePayOrder`, `SUB_MB_GetPayChannel`
- Withdrawal: `SUB_MB_PlaceWithdrawOrder`, `SUB_MB_GetWithdrawRecord`
- Lottery/Wheel: `SUB_MB_GetLotteryCell`, `SUB_MB_BetTreasureChestLoadConfig`
- Tasks: `SUB_MB_Task_Buff_Status`, `SUB_MB_CheckInLoadConfig`
- VIP: `SUB_MB_GetGrowUserStatus`

## Game Launch Flow

`MDM_GAME_LOGON` (100) + `SUB_GAME_APIGAME_LAUNCH` (270). Response contains `urlPath` (utf8[1024]) with the actual game launch URL.

## Bot Detection

### Layer 1: disable-devtool library (by theajack)

Detection methods:
- **Element timing**: Measures time between `console.log`/`console.clear` cycles — automation adds detectable latency
- **Window size**: `window.outerWidth - window.innerWidth > 160`
- **Debugger statement timing**

When triggered:
1. `window.open("about:blank", "_self")` — redirects to blank
2. `window.location.href = "https://theajack.github.io/disable-devtool/..."` — fallback
3. `window.close()` — cleanup

### Layer 2: Native bridge check (St function)

```javascript
St = () => window.jsBridge || window.Native?.getMyDeviceId();
```

Returns falsy outside native app WebView → triggers redirect.

### Observed in headless browsers

- All network requests succeed (200s)
- DOM is empty: `<html><head></head><body></body></html>`
- JS context URL: `about:blank`
- Console: repeating `console.log` + `console.clear` + `console.table` cycles
- Screenshot: ~28KB (partially rendered)

## Python WebSocket Testing

All direct connection attempts failed with:

```
websockets.exceptions.WebSocketException: no close frame received or sent
```

The server accepted the TCP/WebSocket connection but immediately dropped it after receiving the login frame — no response data, no close frame. This is consistent with the server rejecting the frame format rather than a network-level issue.

### Variants tested (all failed identically)

| Variant | SubCmd | Frame Size | IP Field | channelName | plazaVersion |
|---------|--------|-----------|----------|-------------|-------------|
| V1 standard | 2 | 226 bytes | uint8_t[14] zeros | empty | 0 |
| V1 ch="H5" | 2 | 228 bytes | uint8_t[14] zeros | "H5" | 0 |
| V6 | 602 | 1283 bytes | utf8[48] "127.0.0.1" | empty | 0 |
| V6 ch="H5" | 602 | 1283 bytes | utf8[48] "127.0.0.1" | "H5" | 0 |
| V1 plazaVersion=1 | 2 | 226 bytes | uint8_t[14] zeros | empty | 1 |

### Root cause analysis

**Primary theory: allocSendBuffer C++ function adds framing beyond the 4-byte header.** The C++ source path found in the WASM (`/mnt/d/MyProg/hxclient-webasm-network/HxWasmClientWebsocket/src/hxwebsocket.cpp`) suggests the function may prepend:
- A packet length prefix
- A connection/session ID  
- A checksum or sequence number
- Or use a proprietary binary framing format

Without being able to run the WASM (blocked by 44 complex emscripten imports), this framing remains opaque to reverse-engineering from the JS bundles alone.

**Secondary theory: Server expects prior HTTP session state.** The browser calls `GET /api/get_push_config` and `GET /api/cpfservice_info` via HTTP before opening the WebSocket. These may set server-side state (CSRF token, visitor tracking) that the WebSocket handshake validates against. The WebSocket server may reject connections that don't have an established session cookie.

---

## WASM Binary Analysis Methodology

The hxws WASM module (`hxws-1.1.1.0.wasm`, 136,685 bytes) was analyzed using Python's `wasmtime` library:

```bash
pip install wasmtime
python -c "
import wasmtime
with open('hxws.wasm', 'rb') as f:
    module = wasmtime.Module(wasmtime.Engine(), f.read())
for exp in module.exports:
    print(exp.name, exp.type)
"
```

**WASM exports** (22 total):
```
memory, __wasm_call_ctors, __getTypeName, malloc, free,
__indirect_function_table, __original_main, main, fflush,
htonl, htons, ntohs,
emscripten_stack_get_end, emscripten_stack_get_base, strerror,
emscripten_stack_init, emscripten_stack_get_free,
_emscripten_stack_restore, _emscripten_stack_alloc,
emscripten_stack_get_current, __start_em_asm, __stop_em_asm
```

**WASM imports** (44 total, from `env` and `wasi_snapshot_preview1`):
- `emscripten_websocket_send_binary`, `_new`, `_close`, `_delete`
- `emscripten_websocket_set_onopen/onclose/onerror/onmessage_callback_on_thread`
- `_embind_register_class`, `_register_class_function`, `_register_class_constructor`, etc.
- `getaddrinfo` (DNS resolution)
- Various `_emval_*` functions (Emscripten JS bridge)
- wasi: `clock_time_get`, `fd_write`, `fd_close`, `fd_seek`

**Key finding**: The functions `allocSendBuffer`, `getSendBufferSize`, and `sendNetData` are NOT direct WASM exports. They are C++ class methods on `WebsocketClient` registered via **embind** (Emscripten's C++/JS binding library) at runtime when the WASM module's `main()` executes. This means:
- They cannot be called directly from Python without running the full hxws WASM environment
- The embind registration requires all 44 browser imports to be implemented (complex JS bridge functions like `_emval_call`, `_emval_get_method_caller`)
- Running the WASM standalone (via wasmtime/wasmer) is not feasible without reimplementing the entire Emscripten runtime

#### Possible root causes (unresolved)

1. **`allocSendBuffer` C++ function adds framing beyond the 4-byte header** — the WASM binary is compiled from C++ source at `/mnt/d/MyProg/hxclient-webasm-network/HxWasmClientWebsocket/src/hxwebsocket.cpp`. The function may prepend a packet length, connection ID, or checksum not visible in the JS Ku class.

2. **Server expects prior HTTP session state** — the browser calls `GET /api/get_push_config` and `GET /api/cpfservice_info` before opening the WebSocket. These may set server-side session state (CSRF token, visitor tracking) that the WebSocket validates as a handshake.

3. **Server validates origin/referer** — even though `origin` header was set to `https://kkbrio.love` in the WebSocket client, the server may check additional headers or require an established session cookie.

4. **hxws WASM compression layer** — the C++ WASM may apply a proprietary binary encoding/compression that the Ku writer alone doesn't replicate. The `getSendBufferSize()` function hints at a fixed buffer with specific framing overhead.

#### WASM binary format (custom parser)

When standard WASM tools fail, the binary format can be parsed manually:

```python
import struct

def read_leb128(data, offset):
    result = 0
    shift = 0
    while True:
        byte = data[offset]
        result |= (byte & 0x7f) << shift
        offset += 1
        shift += 7
        if not (byte & 0x80):
            break
    return result, offset

# WASM header: magic \\0asm + version
magic = data[:4]  # b'\\x00asm'
version = struct.unpack('<I', data[4:8])[0]

# Sections: id (1 byte) + size (LEB128) + content
offset = 8
while offset < len(data):
    section_id = data[offset]
    offset += 1
    size, offset = read_leb128(data, offset)
    section_end = offset + size
    
    if section_id == 7:  # Export
        count, eb = read_leb128(data, offset)
        for i in range(count):
            nlen, eb = read_leb128(data, eb)
            name = data[eb:eb+nlen].decode('utf-8')
            eb += nlen
            kind = data[eb]; eb += 1
            idx = struct.unpack('<I', data[eb:eb+4])[0]; eb += 4
    
    offset = section_end
```

This approach revealed that the WASM's export section stores name+kind+index tuples. Section ID mapping:
- 1=type, 2=import, 3=function, 4=table, 5=memory, 6=global
- 7=export, 8=start, 9=element, 10=code, 11=data

## Domain Farm

26+ domains for the same service: kkbrio.love, kkbrio.com, kkbrio.co, kkbrio.org, kkbrio.app, kkbrio.blog, kkbrio.one, kkbrio.bar, kkbrio.pro, kkbrio.bet, kkbrio.vip, kkbrio.my, kkbrio.xyz, kkbrio.ac, kkbrio.io, kkbrio.cc, kkbrio.ad, kkbrio.cl, kkbrio.in, kkbrio.club, kkbrio.ae, kkbrio.at, kkbrio.cx, kkbrio.cz, kkbrio.de
