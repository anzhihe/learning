#! /bin/sh
# Strips off the header from a mail/News message i.e. till the first
# empty line
# Mark Moraes, University of Toronto

# ==> These comments added by author of this document.

if [ $# -eq 0 ]; then
# ==> If no command line args present, then works on file redirected to stdin.
	sed -e '1,/^$/d' -e '/^[ 	]*$/d'
	# --> Delete empty lines and all lines until 
	# --> first one beginning with white space.
else
# ==> If command line args present, then work on files named.
	for i do
		sed -e '1,/^$/d' -e '/^[ 	]*$/d' $i
		# --> Ditto, as above.
	done
fi

# ==> Exercise: Add error checking and other options.
# ==>
# ==> Note that the small sed script repeats, except for the arg passed.
# ==> Does it make sense to embed it in a function? Why or why not?
