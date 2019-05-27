#!/bin/bash
# makedict.sh  [make dictionary]

# Modification of /usr/sbin/mkdict script.
# Original script copyright 1993, by Alec Muffett.
#
#  This modified script included in this document in a manner
#+ consistent with the "LICENSE" document of the "Crack" package
#+ that the original script is a part of.

#  This script processes text files to produce a sorted list
#+ of words found in the files.
#  This may be useful for compiling dictionaries
#+ and for lexicographic research.


E_BADARGS=65

if [ ! -r "$1" ]                     #  Need at least one
then                                 #+ valid file argument.
  echo "Usage: $0 files-to-process"
  exit $E_BADARGS
fi  


# SORT="sort"                        #  No longer necessary to define options
                                     #+ to sort. Changed from original script.

cat $* |                             # Contents of specified files to stdout.
        tr A-Z a-z |                 # Convert to lowercase.
        tr ' ' '\012' |              # New: change spaces to newlines.
#       tr -cd '\012[a-z][0-9]' |    #  Get rid of everything non-alphanumeric
                                     #+ (original script).
        tr -c '\012a-z'  '\012' |    #  Rather than deleting
                                     #+ now change non-alpha to newlines.
        sort |                       # $SORT options unnecessary now.
        uniq |                       # Remove duplicates.
        grep -v '^#' |               # Delete lines beginning with a hashmark.
        grep -v '^$'                 # Delete blank lines.

exit 0	
