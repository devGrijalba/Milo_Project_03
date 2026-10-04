#!/usr/bin/env bash
# CDP row health check: one line per port, distinguishing ALIVE / NO_TAB / DEAD.
# Usage: bash scripts/cdp_health.sh 9222:chat.deepseek.com 9223:chatgpt.com
#        bash scripts/cdp_health.sh 9222 9223 9224 9225        (no URL filter)
set -u

status_line() {
  local port="$1" expect="${2:-}"
  local ver tabs hit
  ver=$(curl -s --max-time 3 "http://127.0.0.1:${port}/json/version")
  if ! printf '%s' "$ver" | grep -q '"Browser"'; then
    printf 'puerto %s: DEAD (sin handshake CDP)\n' "$port"
    return
  fi
  local browser
  browser=$(printf '%s' "$ver" | grep -o '"Browser": *"[^"]*"' | sed 's/.*: *//')
  tabs=$(curl -s --max-time 3 "http://127.0.0.1:${port}/json/list")
  if [ -n "$expect" ]; then
    hit=$(printf '%s' "$tabs" | grep -F "\"url\": \"${expect}" | head -1)
    if [ -n "$hit" ]; then
      printf 'puerto %s: OK  %s  tab=%s\n' "$port" "$browser" "$expect"
    else
      printf 'puerto %s: NO_TAB  %s  (proceso vivo, sin pestana %s)\n' "$port" "$browser" "$expect"
    fi
  else
    local pages
    pages=$(printf '%s' "$tabs" | grep -o '"url": *"[^"]*"' \
      | grep -vE 'omnibox|chrome-extension://|devtools://' | wc -l)
    printf 'puerto %s: VIVO  %s  paginas=%s\n' "$port" "$browser" "$pages"
  fi
}

if [ "$#" -eq 0 ]; then
  echo "uso: bash scripts/cdp_health.sh <port[:url-substring]> [...]" >&2
  exit 2
fi

for arg in "$@"; do
  case "$arg" in
    *:*) port="${arg%%:*}"; expect="${arg#*:}" ;;
    *)   port="$arg"; expect="" ;;
  esac
  status_line "$port" "$expect"
done