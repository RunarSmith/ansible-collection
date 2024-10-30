#!/bin/bash

Term="$1"

if [ "x$Term" == "x" ]; then
    echo "Please provide a host to remove !!!"
    exit -1
fi

echo "Removing host -${Term}-"

grep -v "$Term" /etc/hosts > /tmp/hosts
# show diff
diff -d /etc/hosts /tmp/hosts
# set it
sudo mv /tmp/hosts /etc/hosts
