#!/bin/bash
# May need to be invoked with  #!/bin/bash2  on older machines.
#
# Random password generator for Bash 2.x by Antek Sawicki &lt;tenox@tenox.tc&gt;,
# who generously gave permission to the document author to use it here.
#
# ==> Comments added by document author ==>


MATRIX="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# ==> Password will consist of alphanumeric characters.
LENGTH="8"
# ==> May change 'LENGTH' for longer password.


while [ "${n:=1}" -le "$LENGTH" ]
# ==> Recall that := is "default substitution" operator.
# ==> So, if 'n' has not been initialized, set it to 1.
do
	PASS="$PASS${MATRIX:$(($RANDOM%${#MATRIX})):1}"
	# ==> Very clever, but tricky.

	# ==> Starting from the innermost nesting...
	# ==> ${#MATRIX} returns length of array MATRIX.

	# ==> $RANDOM%${#MATRIX} returns random number between 1
	# ==> and [length of MATRIX] - 1.

	# ==> ${MATRIX:$(($RANDOM%${#MATRIX})):1}
	# ==> returns expansion of MATRIX at random position, by length 1. 
	# ==> See {var:pos:len} parameter substitution in Chapter 9.
	# ==> and the associated examples.

	# ==> PASS=... simply pastes this result onto previous PASS (concatenation).

	# ==> To visualize this more clearly, uncomment the following line
	#                 echo "$PASS"
	# ==> to see PASS being built up,
	# ==> one character at a time, each iteration of the loop.

	let n+=1
	# ==> Increment 'n' for next pass.
done

echo "$PASS"      # ==> Or, redirect to a file, as desired.

exit 0
