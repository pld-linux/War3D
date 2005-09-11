#!/bin/sh

CONF="$HOME/.War3D.conf"

cd /usr/share/War3D

[ -r "$CONF" ] || cp -f War3D.conf $CONF

exec war3d.bin
