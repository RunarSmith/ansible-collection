#!/bin/bash

# Just a wrapper to workaround a bug in firefox or X11 :
# https://bugzilla.mozilla.org/show_bug.cgi?id=1033721

# When using firefox over a SSH connection with X11Forward, firefox hangs :(

killall firefox
killall firefox-esr

firefox --new-instance --no-remote --disable-pinch $*
