#!/bin/bash

#echo $0
#pidof sh 12-01spawn.sh
echo "\$\$: $$"
PIDS=$(pidof bash $0)
P_array=( $PIDS )
echo "PIDS: $PIDS"

let  "instances = ${#P_array[*]}-1"
echo "$instances instance(s) of this script running."
echo "[Hit Ctrl+C to exit.]" ; echo

sleep 1
bash $0

exit 0
