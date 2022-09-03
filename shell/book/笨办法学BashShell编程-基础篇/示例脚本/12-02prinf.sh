#!/bin/bash

PI=3.14159265358979
DecimalConstant=12345
Message1="Greetings,"
Message2="Erthling."

echo
printf "Pi to 2 decimal places =%1.2f" $PI
echo
printf "Pi to 2 decimal places =%1.9f" $PI

echo
printf "\n"

echo
printf "Constant = \t%d\n" $EecimalConstant

echo
printf "%s %s \n" $Message1 $Message2

exit 0
