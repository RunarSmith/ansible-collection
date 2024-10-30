#!/bin/bash

if [[ $# -eq 0 ]]; then
  # without parameters, list config files
  echo "available VPN config files :"
  echo ""
  ls -1 ~/.vpn
  exit 0
fi

# a parameter is provided, use it

Filter=$1

vpnfile=$(ls /home/user/.vpn/*${Filter}*.ovpn)

sudo openvpn --config "${vpnfile}" --log-append /var/log/openvpn/vpn.log &

