#!/bin/bash
# obj-oriented.sh: Object-oriented programming in a shell script.
# Script by Stephane Chazelas.

#  Important Note:
#  --------- ----
#  If running this script under version 3 or later of Bash,
#+ replace all periods in function names with a "legal" character,
#+ for example, an underscore.


person.new()        # Looks almost like a class declaration in C++.
{
  local obj_name=$1 name=$2 firstname=$3 birthdate=$4

  eval "$obj_name.set_name() {
          eval \"$obj_name.get_name() {
                   echo \$1
                 }\"
        }"

  eval "$obj_name.set_firstname() {
          eval \"$obj_name.get_firstname() {
                   echo \$1
                 }\"
        }"

  eval "$obj_name.set_birthdate() {
          eval \"$obj_name.get_birthdate() {
            echo \$1
          }\"
          eval \"$obj_name.show_birthdate() {
            echo \$(date -d \"1/1/1970 0:0:\$1 GMT\")
          }\"
          eval \"$obj_name.get_age() {
            echo \$(( (\$(date +%s) - \$1) / 3600 / 24 / 365 ))
          }\"
        }"

  $obj_name.set_name $name
  $obj_name.set_firstname $firstname
  $obj_name.set_birthdate $birthdate
}

echo

person.new self Bozeman Bozo 101272413
# Create an instance of "person.new" (actually passing args to the function).

self.get_firstname       #   Bozo
self.get_name            #   Bozeman
self.get_age             #   28
self.get_birthdate       #   101272413
self.show_birthdate      #   Sat Mar 17 20:13:33 MST 1973

echo

#  typeset -f
#+ to see the created functions (careful, it scrolls off the page).

exit 0
