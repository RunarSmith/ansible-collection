#!/bin/bash

# https://portswigger.net/burp/documentation/desktop/external-browser-config/certificate/ca-cert-firefox
# we have to start BS, wait for it to be started, and download the cacert

rm -f /tmp/cacert.der

/bin/bash -c "timeout 35 /usr/share/burpsuite/jre/bin/java -Djava.awt.headless=true -jar /usr/share/burpsuite/burpsuite_community.jar < <(echo y) &" 
sleep 30

curl -s http://localhost:8080/cert -o /tmp/cacert.der

exit
