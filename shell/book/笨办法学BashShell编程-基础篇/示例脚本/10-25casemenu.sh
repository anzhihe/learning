#!/bin/bash
clear

echo "Contact List"
echo "------------"
echo
echo "[E]vans, Roland"
echo "[J]ones, Mildred"
echo "[S]mith, Julie"
echo

read person

case "$person" in
  "E" | "e" )
    echo "Evans, Roland"
    echo "(010)6123456"
    ;;

  "J" | "j" )
    echo "Jones, Mildred"
    echo "(020)6938946"
    ;;

  "S" | "s" )
    echo "Smith, Julie"
    echo "(03)6123456"
    ;;

  * )
    echo 
    echo "Not yet in database."
    ;;
esac
echo
exit 0

