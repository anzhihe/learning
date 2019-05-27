#!/bin/bash
# life.sh: "Life in the Slow Lane"
# Version 2: Patched by Daniel Albers
#+           to allow non-square grids as input.

# ##################################################################### #
# This is the Bash script version of John Conway's "Game of Life".      #
# "Life" is a simple implementation of cellular automata.               #
# --------------------------------------------------------------------- #
# On a rectangular grid, let each "cell" be either "living" or "dead".  #
# Designate a living cell with a dot, and a dead one with a blank space.#
#  Begin with an arbitrarily drawn dot-and-blank grid,                  #
#+ and let this be the starting generation, "generation 0".             #
# Determine each successive generation by the following rules:          #
# 1) Each cell has 8 neighbors, the adjoining cells                     #
#+   left, right, top, bottom, and the 4 diagonals.                     #
#                       123                                             #
#                       4*5                                             #
#                       678                                             #
#                                                                       #
# 2) A living cell with either 2 or 3 living neighbors remains alive.   #
# 3) A dead cell with 3 living neighbors becomes alive (a "birth").     #
SURVIVE=2                                                               #
BIRTH=3                                                                 #
# 4) All other cases result in a dead cell for the next generation.     #
# ##################################################################### #


startfile=gen0   # Read the starting generation from the file "gen0".
                 # Default, if no other file specified when invoking script.
                 #
if [ -n "$1" ]   # Specify another "generation 0" file.
then
    startfile="$1"
fi  

############################################
#  Abort script if "startfile" not specified
#+ AND
#+ "gen0" not present.

E_NOSTARTFILE=68

if [ ! -e "$startfile" ]
then
  echo "Startfile \""$startfile"\" missing!"
  exit $E_NOSTARTFILE
fi
############################################


ALIVE1=.
DEAD1=_
                 # Represent living and "dead" cells in the start-up file.

#  ---------------------------------------------------------- #
#  This script uses a 10 x 10 grid (may be increased,
#+ but a large grid will will cause very slow execution).
ROWS=10
COLS=10
#  Change above two variables to match grid size, if necessary.
#  ---------------------------------------------------------- #

GENERATIONS=10          #  How many generations to cycle through.
                        #  Adjust this upwards,
                        #+ if you have time on your hands.

NONE_ALIVE=80           #  Exit status on premature bailout,
                        #+ if no cells left alive.
TRUE=0
FALSE=1
ALIVE=0
DEAD=1

avar=                   # Global; holds current generation.
generation=0            # Initialize generation count.

# =================================================================


let "cells = $ROWS * $COLS"
                        # How many cells.

declare -a initial      # Arrays containing "cells".
declare -a current

display ()
{

alive=0                 # How many cells "alive" at any given time.
                        # Initially zero.

declare -a arr
arr=( `echo "$1"` )     # Convert passed arg to array.

element_count=${#arr[*]}

local i
local rowcheck

for ((i=0; i<$element_count; i++))
do

  # Insert newline at end of each row.
  let "rowcheck = $i % COLS"
  if [ "$rowcheck" -eq 0 ]
  then
    echo                # Newline.
    echo -n "      "    # Indent.
  fi  

  cell=${arr[i]}

  if [ "$cell" = . ]
  then
    let "alive += 1"
  fi  

  echo -n "$cell" | sed -e 's/_/ /g'
  # Print out array and change underscores to spaces.
done  

return

}

IsValid ()                            # Test whether cell coordinate valid.
{

  if [ -z "$1"  -o -z "$2" ]          # Mandatory arguments missing?
  then
    return $FALSE
  fi

local row
local lower_limit=0                   # Disallow negative coordinate.
local upper_limit
local left
local right

let "upper_limit = $ROWS * $COLS - 1" # Total number of cells.


if [ "$1" -lt "$lower_limit" -o "$1" -gt "$upper_limit" ]
then
  return $FALSE                       # Out of array bounds.
fi  

row=$2
let "left = $row * $COLS"             # Left limit.
let "right = $left + $COLS - 1"       # Right limit.

if [ "$1" -lt "$left" -o "$1" -gt "$right" ]
then
  return $FALSE                       # Beyond row boundary.
fi  

return $TRUE                          # Valid coordinate.

}  


IsAlive ()              # Test whether cell is alive.
                        # Takes array, cell number, state of cell as arguments.
{
  GetCount "$1" $2      # Get alive cell count in neighborhood.
  local nhbd=$?


  if [ "$nhbd" -eq "$BIRTH" ]  # Alive in any case.
  then
    return $ALIVE
  fi

  if [ "$3" = "." -a "$nhbd" -eq "$SURVIVE" ]
  then                  # Alive only if previously alive.
    return $ALIVE
  fi  

  return $DEAD          # Default.

}  


GetCount ()             # Count live cells in passed cell's neighborhood.
                        # Two arguments needed:
			# $1) variable holding array
			# $2) cell number
{
  local cell_number=$2
  local array
  local top
  local center
  local bottom
  local r
  local row
  local i
  local t_top
  local t_cen
  local t_bot
  local count=0
  local ROW_NHBD=3

  array=( `echo "$1"` )

  let "top = $cell_number - $COLS - 1"    # Set up cell neighborhood.
  let "center = $cell_number - 1"
  let "bottom = $cell_number + $COLS - 1"
  let "r = $cell_number / $COLS"

  for ((i=0; i<$ROW_NHBD; i++))           # Traverse from left to right. 
  do
    let "t_top = $top + $i"
    let "t_cen = $center + $i"
    let "t_bot = $bottom + $i"


    let "row = $r"                        # Count center row of neighborhood.
    IsValid $t_cen $row                   # Valid cell position?
    if [ $? -eq "$TRUE" ]
    then
      if [ ${array[$t_cen]} = "$ALIVE1" ] # Is it alive?
      then                                # Yes?
        let "count += 1"                  # Increment count.
      fi	
    fi  

    let "row = $r - 1"                    # Count top row.          
    IsValid $t_top $row
    if [ $? -eq "$TRUE" ]
    then
      if [ ${array[$t_top]} = "$ALIVE1" ] 
      then
        let "count += 1"
      fi	
    fi  

    let "row = $r + 1"                    # Count bottom row.
    IsValid $t_bot $row
    if [ $? -eq "$TRUE" ]
    then
      if [ ${array[$t_bot]} = "$ALIVE1" ] 
      then
        let "count += 1"
      fi	
    fi  

  done  


  if [ ${array[$cell_number]} = "$ALIVE1" ]
  then
    let "count -= 1"        #  Make sure value of tested cell itself
  fi                        #+ is not counted.


  return $count
  
}

next_gen ()               # Update generation array.
{

local array
local i=0

array=( `echo "$1"` )     # Convert passed arg to array.

while [ "$i" -lt "$cells" ]
do
  IsAlive "$1" $i ${array[$i]}   # Is cell alive?
  if [ $? -eq "$ALIVE" ]
  then                           #  If alive, then
    array[$i]=.                  #+ represent the cell as a period.
  else  
    array[$i]="_"                #  Otherwise underscore
   fi                            #+ (which will later be converted to space).  
  let "i += 1" 
done   


# let "generation += 1"   # Increment generation count.
# Why was the above line commented out?


# Set variable to pass as parameter to "display" function.
avar=`echo ${array[@]}`   # Convert array back to string variable.
display "$avar"           # Display it.
echo; echo
echo "Generation $generation  -  $alive alive"

if [ "$alive" -eq 0 ]
then
  echo
  echo "Premature exit: no more cells alive!"
  exit $NONE_ALIVE        #  No point in continuing
fi                        #+ if no live cells.

}


# =========================================================

# main ()

# Load initial array with contents of startup file.
initial=( `cat "$startfile" | sed -e '/#/d' | tr -d '\n' |\
sed -e 's/\./\. /g' -e 's/_/_ /g'` )
# Delete lines containing '#' comment character.
# Remove linefeeds and insert space between elements.

clear          # Clear screen.

echo #         Title
echo "======================="
echo "    $GENERATIONS generations"
echo "           of"
echo "\"Life in the Slow Lane\""
echo "======================="


# -------- Display first generation. --------
Gen0=`echo ${initial[@]}`
display "$Gen0"           # Display only.
echo; echo
echo "Generation $generation  -  $alive alive"
# -------------------------------------------


let "generation += 1"     # Increment generation count.
echo

# ------- Display second generation. -------
Cur=`echo ${initial[@]}`
next_gen "$Cur"          # Update & display.
# ------------------------------------------

let "generation += 1"     # Increment generation count.

# ------ Main loop for displaying subsequent generations ------
while [ "$generation" -le "$GENERATIONS" ]
do
  Cur="$avar"
  next_gen "$Cur"
  let "generation += 1"
done
# ==============================================================

echo

exit 0   # END



# The grid in this script has a "boundary problem."
# The the top, bottom, and sides border on a void of dead cells.
# Exercise: Change the script to have the grid wrap around,
# +         so that the left and right sides will "touch,"      
# +         as will the top and bottom.
#
# Exercise: Create a new "gen0" file to seed this script.
#           Use a 12 x 16 grid, instead of the original 10 x 10 one.
#           Make the necessary changes to the script,
#+          so it will run with the altered file.
#
# Exercise: Modify this script so that it can determine the grid size
#+          from the "gen0" file, and set any variables necessary
#+          for the script to run.
#           This would make unnecessary any changes to variables
#+          in the script for an altered grid size.
