#!/bin/bash

sudo tail -n20 /var/log/openvpn/vpn.log

# show IP addresses and network interfaces
echo ""
ip -br -c a s
