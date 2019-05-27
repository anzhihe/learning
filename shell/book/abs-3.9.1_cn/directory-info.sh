#! /bin/bash
# directory-info.sh
# Parses and lists directory information.

# NOTE: Change lines 273 and 353 per "README" file.

# Michael Zick is the author of this script.
# Used here with his permission.

# Controls
# If overridden by command arguments, they must be in the order:
#   Arg1: "Descriptor Directory"
#   Arg2: "Exclude Paths"
#   Arg3: "Exclude Directories"
#
# Environment Settings override Defaults.
# Command arguments override Environment Settings.

# Default location for content addressed file descriptors.
MD5UCFS=${1:-${MD5UCFS:-'/tmpfs/ucfs'}}

# Directory paths never to list or enter
declare -a \
  EXCLUDE_PATHS=${2:-${EXCLUDE_PATHS:-'(/proc /dev /devfs /tmpfs)'}}

# Directories never to list or enter
declare -a \
  EXCLUDE_DIRS=${3:-${EXCLUDE_DIRS:-'(ucfs lost+found tmp wtmp)'}}

# Files never to list or enter
declare -a \
  EXCLUDE_FILES=${3:-${EXCLUDE_FILES:-'(core "Name with Spaces")'}}


# Here document used as a comment block.
: &lt;&lt;LSfieldsDoc
# # # # # List Filesystem Directory Information # # # # #
#
#	ListDirectory "FileGlob" "Field-Array-Name"
# or
#	ListDirectory -of "FileGlob" "Field-Array-Filename"
#	'-of' meaning 'output to filename'
# # # # #

String format description based on: ls (GNU fileutils) version 4.0.36

Produces a line (or more) formatted:
inode permissions hard-links owner group ...
32736 -rw-------    1 mszick   mszick

size    day month date hh:mm:ss year path
2756608 Sun Apr 20 08:53:06 2003 /home/mszick/core

Unless it is formatted:
inode permissions hard-links owner group ...
266705 crw-rw----    1    root  uucp

major minor day month date hh:mm:ss year path
4,  68 Sun Apr 20 09:27:33 2003 /dev/ttyS4
NOTE: that pesky comma after the major number

NOTE: the 'path' may be multiple fields:
/home/mszick/core
/proc/982/fd/0 -> /dev/null
/proc/982/fd/1 -> /home/mszick/.xsession-errors
/proc/982/fd/13 -> /tmp/tmpfZVVOCs (deleted)
/proc/982/fd/7 -> /tmp/kde-mszick/ksycoca
/proc/982/fd/8 -> socket:[11586]
/proc/982/fd/9 -> pipe:[11588]

If that isn't enough to keep your parser guessing,
either or both of the path components may be relative:
../Built-Shared -> Built-Static
../linux-2.4.20.tar.bz2 -> ../../../SRCS/linux-2.4.20.tar.bz2

The first character of the 11 (10?) character permissions field:
's' Socket
'd' Directory
'b' Block device
'c' Character device
'l' Symbolic link
NOTE: Hard links not marked - test for identical inode numbers
on identical filesystems.
All information about hard linked files are shared, except
for the names and the name's location in the directory system.
NOTE: A "Hard link" is known as a "File Alias" on some systems.
'-' An undistingushed file

Followed by three groups of letters for: User, Group, Others
Character 1: '-' Not readable; 'r' Readable
Character 2: '-' Not writable; 'w' Writable
Character 3, User and Group: Combined execute and special
'-' Not Executable, Not Special
'x' Executable, Not Special
's' Executable, Special
'S' Not Executable, Special
Character 3, Others: Combined execute and sticky (tacky?)
'-' Not Executable, Not Tacky
'x' Executable, Not Tacky
't' Executable, Tacky
'T' Not Executable, Tacky

Followed by an access indicator
Haven't tested this one, it may be the eleventh character
or it may generate another field
' ' No alternate access
'+' Alternate access
LSfieldsDoc


ListDirectory()
{
	local -a T
	local -i of=0		# Default return in variable
#	OLD_IFS=$IFS		# Using BASH default ' \t\n'

	case "$#" in
	3)	case "$1" in
		-of)	of=1 ; shift ;;
		 * )	return 1 ;;
		esac ;;
	2)	: ;;		# Poor man's "continue"
	*)	return 1 ;;
	esac

	# NOTE: the (ls) command is NOT quoted (")
	T=( $(ls --inode --ignore-backups --almost-all --directory \
	--full-time --color=none --time=status --sort=none \
	--format=long $1) )

	case $of in
	# Assign T back to the array whose name was passed as $2
		0) eval $2=\( \"\$\{T\[@\]\}\" \) ;;
	# Write T into filename passed as $2
		1) echo "${T[@]}" > "$2" ;;
	esac
	return 0
   }

# # # # # Is that string a legal number? # # # # #
#
#	IsNumber "Var"
# # # # # There has to be a better way, sigh...

IsNumber()
{
	local -i int
	if [ $# -eq 0 ]
	then
		return 1
	else
		(let int=$1)  2>/dev/null
		return $?	# Exit status of the let thread
	fi
}

# # # # # Index Filesystem Directory Information # # # # #
#
#	IndexList "Field-Array-Name" "Index-Array-Name"
# or
#	IndexList -if Field-Array-Filename Index-Array-Name
#	IndexList -of Field-Array-Name Index-Array-Filename
#	IndexList -if -of Field-Array-Filename Index-Array-Filename
# # # # #

: &lt;&lt;IndexListDoc
Walk an array of directory fields produced by ListDirectory

Having suppressed the line breaks in an otherwise line oriented
report, build an index to the array element which starts each line.

Each line gets two index entries, the first element of each line
(inode) and the element that holds the pathname of the file.

The first index entry pair (Line-Number==0) are informational:
Index-Array-Name[0] : Number of "Lines" indexed
Index-Array-Name[1] : "Current Line" pointer into Index-Array-Name

The following index pairs (if any) hold element indexes into
the Field-Array-Name per:
Index-Array-Name[Line-Number * 2] : The "inode" field element.
NOTE: This distance may be either +11 or +12 elements.
Index-Array-Name[(Line-Number * 2) + 1] : The "pathname" element.
NOTE: This distance may be a variable number of elements.
Next line index pair for Line-Number+1.
IndexListDoc



IndexList()
{
	local -a LIST			# Local of listname passed
	local -a -i INDEX=( 0 0 )	# Local of index to return
	local -i Lidx Lcnt
	local -i if=0 of=0		# Default to variable names

	case "$#" in			# Simplistic option testing
		0) return 1 ;;
		1) return 1 ;;
		2) : ;;			# Poor man's continue
		3) case "$1" in
			-if) if=1 ;;
			-of) of=1 ;;
			 * ) return 1 ;;
		   esac ; shift ;;
		4) if=1 ; of=1 ; shift ; shift ;;
		*) return 1
	esac

	# Make local copy of list
	case "$if" in
		0) eval LIST=\( \"\$\{$1\[@\]\}\" \) ;;
		1) LIST=( $(cat $1) ) ;;
	esac

	# Grok (grope?) the array
	Lcnt=${#LIST[@]}
	Lidx=0
	until (( Lidx >= Lcnt ))
	do
	if IsNumber ${LIST[$Lidx]}
	then
		local -i inode name
		local ft
		inode=Lidx
		local m=${LIST[$Lidx+2]}	# Hard Links field
		ft=${LIST[$Lidx+1]:0:1} 	# Fast-Stat
		case $ft in
		b)	((Lidx+=12)) ;;		# Block device
		c)	((Lidx+=12)) ;;		# Character device
		*)	((Lidx+=11)) ;;		# Anything else
		esac
		name=Lidx
		case $ft in
		-)	((Lidx+=1)) ;;		# The easy one
		b)	((Lidx+=1)) ;;		# Block device
		c)	((Lidx+=1)) ;;		# Character device
		d)	((Lidx+=1)) ;;		# The other easy one
		l)	((Lidx+=3)) ;;		# At LEAST two more fields
#  A little more elegance here would handle pipes,
#+ sockets, deleted files - later.
		*)	until IsNumber ${LIST[$Lidx]} || ((Lidx >= Lcnt))
			do
				((Lidx+=1))
			done
			;;			# Not required
		esac
		INDEX[${#INDEX[*]}]=$inode
		INDEX[${#INDEX[*]}]=$name
		INDEX[0]=${INDEX[0]}+1		# One more "line" found
# echo "Line: ${INDEX[0]} Type: $ft Links: $m Inode: \
# ${LIST[$inode]} Name: ${LIST[$name]}"

	else
		((Lidx+=1))
	fi
	done
	case "$of" in
		0) eval $2=\( \"\$\{INDEX\[@\]\}\" \) ;;
		1) echo "${INDEX[@]}" > "$2" ;;
	esac
	return 0				# What could go wrong?
}

# # # # # Content Identify File # # # # #
#
#	DigestFile Input-Array-Name Digest-Array-Name
# or
#	DigestFile -if Input-FileName Digest-Array-Name
# # # # #

# Here document used as a comment block.
: &lt;&lt;DigestFilesDoc

The key (no pun intended) to a Unified Content File System (UCFS)
is to distinguish the files in the system based on their content.
Distinguishing files by their name is just, so, 20th Century.

The content is distinguished by computing a checksum of that content.
This version uses the md5sum program to generate a 128 bit checksum
representative of the file's contents.
There is a chance that two files having different content might
generate the same checksum using md5sum (or any checksum).  Should
that become a problem, then the use of md5sum can be replace by a
cyrptographic signature.  But until then...

The md5sum program is documented as outputting three fields (and it
does), but when read it appears as two fields (array elements).  This
is caused by the lack of whitespace between the second and third field.
So this function gropes the md5sum output and returns:
	[0]	32 character checksum in hexidecimal (UCFS filename)
	[1]	Single character: ' ' text file, '*' binary file
	[2]	Filesystem (20th Century Style) name
	Note: That name may be the character '-' indicating STDIN read.

DigestFilesDoc



DigestFile()
{
	local if=0		# Default, variable name
	local -a T1 T2

	case "$#" in
	3)	case "$1" in
		-if)	if=1 ; shift ;;
		 * )	return 1 ;;
		esac ;;
	2)	: ;;		# Poor man's "continue"
	*)	return 1 ;;
	esac

	case $if in
	0) eval T1=\( \"\$\{$1\[@\]\}\" \)
	   T2=( $(echo ${T1[@]} | md5sum -) )
	   ;;
	1) T2=( $(md5sum $1) )
	   ;;
	esac

	case ${#T2[@]} in
	0) return 1 ;;
	1) return 1 ;;
	2) case ${T2[1]:0:1} in		# SanScrit-2.0.5
	   \*) T2[${#T2[@]}]=${T2[1]:1}
	       T2[1]=\*
	       ;;
	    *) T2[${#T2[@]}]=${T2[1]}
	       T2[1]=" "
	       ;;
	   esac
	   ;;
	3) : ;; # Assume it worked
	*) return 1 ;;
	esac

	local -i len=${#T2[0]}
	if [ $len -ne 32 ] ; then return 1 ; fi
	eval $2=\( \"\$\{T2\[@\]\}\" \)
}

# # # # # Locate File # # # # #
#
#	LocateFile [-l] FileName Location-Array-Name
# or
#	LocateFile [-l] -of FileName Location-Array-FileName
# # # # #

# A file location is Filesystem-id and inode-number

# Here document used as a comment block.
: &lt;&lt;StatFieldsDoc
	Based on stat, version 2.2
	stat -t and stat -lt fields
	[0]	name
	[1]	Total size
		File - number of bytes
		Symbolic link - string length of pathname
	[2]	Number of (512 byte) blocks allocated
	[3]	File type and Access rights (hex)
	[4]	User ID of owner
	[5]	Group ID of owner
	[6]	Device number
	[7]	Inode number
	[8]	Number of hard links
	[9]	Device type (if inode device) Major
	[10]	Device type (if inode device) Minor
	[11]	Time of last access
		May be disabled in 'mount' with noatime
		atime of files changed by exec, read, pipe, utime, mknod (mmap?)
		atime of directories changed by addition/deletion of files
	[12]	Time of last modification
		mtime of files changed by write, truncate, utime, mknod
		mtime of directories changed by addtition/deletion of files
	[13]	Time of last change
		ctime reflects time of changed inode information (owner, group
		permissions, link count
-*-*- Per:
	Return code: 0
	Size of array: 14
	Contents of array
	Element 0: /home/mszick
	Element 1: 4096
	Element 2: 8
	Element 3: 41e8
	Element 4: 500
	Element 5: 500
	Element 6: 303
	Element 7: 32385
	Element 8: 22
	Element 9: 0
	Element 10: 0
	Element 11: 1051221030
	Element 12: 1051214068
	Element 13: 1051214068

	For a link in the form of linkname -> realname
	stat -t  linkname returns the linkname (link) information
	stat -lt linkname returns the realname information

	stat -tf and stat -ltf fields
	[0]	name
	[1]	ID-0?		# Maybe someday, but Linux stat structure
	[2]	ID-0?		# does not have either LABEL nor UUID
				# fields, currently information must come
				# from file-system specific utilities
	These will be munged into:
	[1]	UUID if possible
	[2]	Volume Label if possible
	Note: 'mount -l' does return the label and could return the UUID

	[3]	Maximum length of filenames
	[4]	Filesystem type
	[5]	Total blocks in the filesystem
	[6]	Free blocks
	[7]	Free blocks for non-root user(s)
	[8]	Block size of the filesystem
	[9]	Total inodes
	[10]	Free inodes

-*-*- Per:
	Return code: 0
	Size of array: 11
	Contents of array
	Element 0: /home/mszick
	Element 1: 0
	Element 2: 0
	Element 3: 255
	Element 4: ef53
	Element 5: 2581445
	Element 6: 2277180
	Element 7: 2146050
	Element 8: 4096
	Element 9: 1311552
	Element 10: 1276425

StatFieldsDoc


#	LocateFile [-l] FileName Location-Array-Name
#	LocateFile [-l] -of FileName Location-Array-FileName

LocateFile()
{
	local -a LOC LOC1 LOC2
	local lk="" of=0

	case "$#" in
	0) return 1 ;;
	1) return 1 ;;
	2) : ;;
	*) while (( "$#" > 2 ))
	   do
	      case "$1" in
	       -l) lk=-1 ;;
	      -of) of=1 ;;
	        *) return 1 ;;
	      esac
	   shift
           done ;;
	esac

# More Sanscrit-2.0.5
      # LOC1=( $(stat -t $lk $1) )
      # LOC2=( $(stat -tf $lk $1) )
      # Uncomment above two lines if system has "stat" command installed.
	LOC=( ${LOC1[@]:0:1} ${LOC1[@]:3:11}
	      ${LOC2[@]:1:2} ${LOC2[@]:4:1} )

	case "$of" in
		0) eval $2=\( \"\$\{LOC\[@\]\}\" \) ;;
		1) echo "${LOC[@]}" > "$2" ;;
	esac
	return 0
# Which yields (if you are lucky, and have "stat" installed)
# -*-*- Location Discriptor -*-*-
#	Return code: 0
#	Size of array: 15
#	Contents of array
#	Element 0: /home/mszick		20th Century name
#	Element 1: 41e8			Type and Permissions
#	Element 2: 500			User
#	Element 3: 500			Group
#	Element 4: 303			Device
#	Element 5: 32385		inode
#	Element 6: 22			Link count
#	Element 7: 0			Device Major
#	Element 8: 0			Device Minor
#	Element 9: 1051224608		Last Access
#	Element 10: 1051214068		Last Modify
#	Element 11: 1051214068		Last Status
#	Element 12: 0			UUID (to be)
#	Element 13: 0			Volume Label (to be)
#	Element 14: ef53		Filesystem type
}



# And then there was some test code

ListArray() # ListArray Name
{
	local -a Ta

	eval Ta=\( \"\$\{$1\[@\]\}\" \)
	echo
	echo "-*-*- List of Array -*-*-"
	echo "Size of array $1: ${#Ta[*]}"
	echo "Contents of array $1:"
	for (( i=0 ; i<${#Ta[*]} ; i++ ))
	do
	    echo -e "\tElement $i: ${Ta[$i]}"
	done
	return 0
}

declare -a CUR_DIR
# For small arrays
ListDirectory "${PWD}" CUR_DIR
ListArray CUR_DIR

declare -a DIR_DIG
DigestFile CUR_DIR DIR_DIG
echo "The new \"name\" (checksum) for ${CUR_DIR[9]} is ${DIR_DIG[0]}"

declare -a DIR_ENT
# BIG_DIR # For really big arrays - use a temporary file in ramdisk
# BIG-DIR # ListDirectory -of "${CUR_DIR[11]}/*" "/tmpfs/junk2"
ListDirectory "${CUR_DIR[11]}/*" DIR_ENT

declare -a DIR_IDX
# BIG-DIR # IndexList -if "/tmpfs/junk2" DIR_IDX
IndexList DIR_ENT DIR_IDX

declare -a IDX_DIG
# BIG-DIR # DIR_ENT=( $(cat /tmpfs/junk2) )
# BIG-DIR # DigestFile -if /tmpfs/junk2 IDX_DIG
DigestFile DIR_ENT IDX_DIG
# Small (should) be able to parallize IndexList & DigestFile
# Large (should) be able to parallize IndexList & DigestFile & the assignment
echo "The \"name\" (checksum) for the contents of ${PWD} is ${IDX_DIG[0]}"

declare -a FILE_LOC
LocateFile ${PWD} FILE_LOC
ListArray FILE_LOC

exit 0
