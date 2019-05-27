#! /bin/sh 
# $Id: ftpget,v 1.2 91/05/07 21:15:43 moraes Exp $ 
# Script to perform batch anonymous ftp. Essentially converts a list of
# of command line arguments into input to ftp.
# ==> This script is nothing but a shell wrapper around "ftp" . . .
# Simple, and quick - written as a companion to ftplist 
# -h specifies the remote host (default prep.ai.mit.edu) 
# -d specifies the remote directory to cd to - you can provide a sequence 
# of -d options - they will be cd'ed to in turn. If the paths are relative, 
# make sure you get the sequence right. Be careful with relative paths - 
# there are far too many symlinks nowadays.  
# (default is the ftp login directory)
# -v turns on the verbose option of ftp, and shows all responses from the 
# ftp server.  
# -f remotefile[:localfile] gets the remote file into localfile 
# -m pattern does an mget with the specified pattern. Remember to quote 
# shell characters.  
# -c does a local cd to the specified directory
# For example, 
# 	ftpget -h expo.lcs.mit.edu -d contrib -f xplaces.shar:xplaces.sh \
#		-d ../pub/R3/fixes -c ~/fixes -m 'fix*' 
# will get xplaces.shar from ~ftp/contrib on expo.lcs.mit.edu, and put it in
# xplaces.sh in the current working directory, and get all fixes from
# ~ftp/pub/R3/fixes and put them in the ~/fixes directory. 
# Obviously, the sequence of the options is important, since the equivalent
# commands are executed by ftp in corresponding order
#
# Mark Moraes &lt;moraes@csri.toronto.edu&gt;, Feb 1, 1989 
#


# ==> These comments added by author of this document.

# PATH=/local/bin:/usr/ucb:/usr/bin:/bin
# export PATH
# ==> Above 2 lines from original script probably superfluous.

E_BADARGS=65

TMPFILE=/tmp/ftp.$$
# ==> Creates temp file, using process id of script ($$)
# ==> to construct filename.

SITE=`domainname`.toronto.edu
# ==> 'domainname' similar to 'hostname'
# ==> May rewrite this to parameterize this for general use.

usage="Usage: $0 [-h remotehost] [-d remotedirectory]... [-f remfile:localfile]... \
		[-c localdirectory] [-m filepattern] [-v]"
ftpflags="-i -n"
verbflag=
set -f 		# So we can use globbing in -m
set x `getopt vh:d:c:m:f: $*`
if [ $? != 0 ]; then
	echo $usage
	exit $E_BADARGS
fi
shift
trap 'rm -f ${TMPFILE} ; exit' 0 1 2 3 15
# ==> Delete tempfile in case of abnormal exit from script.
echo "user anonymous ${USER-gnu}@${SITE} > ${TMPFILE}"
# ==> Added quotes (recommended in complex echoes).
echo binary >> ${TMPFILE}
for i in $*   # ==> Parse command line args.
do
	case $i in
	-v) verbflag=-v; echo hash >> ${TMPFILE}; shift;;
	-h) remhost=$2; shift 2;;
	-d) echo cd $2 >> ${TMPFILE}; 
	    if [ x${verbflag} != x ]; then
	        echo pwd >> ${TMPFILE};
	    fi;
	    shift 2;;
	-c) echo lcd $2 >> ${TMPFILE}; shift 2;;
	-m) echo mget "$2" >> ${TMPFILE}; shift 2;;
	-f) f1=`expr "$2" : "\([^:]*\).*"`; f2=`expr "$2" : "[^:]*:\(.*\)"`;
	    echo get ${f1} ${f2} >> ${TMPFILE}; shift 2;;
	--) shift; break;;
	esac
        # ==> 'lcd' and 'mget' are ftp commands. See "man ftp" . . .
done
if [ $# -ne 0 ]; then
	echo $usage
	exit $E_BADARGS
        # ==> Changed from "exit 2" to conform with style standard.
fi
if [ x${verbflag} != x ]; then
	ftpflags="${ftpflags} -v"
fi
if [ x${remhost} = x ]; then
	remhost=prep.ai.mit.edu
	# ==> Change to match appropriate ftp site.
fi
echo quit >> ${TMPFILE}
# ==> All commands saved in tempfile.

ftp ${ftpflags} ${remhost} < ${TMPFILE}
# ==> Now, tempfile batch processed by ftp.

rm -f ${TMPFILE}
# ==> Finally, tempfile deleted (you may wish to copy it to a logfile).


# ==> Exercises:
# ==> ---------
# ==> 1) Add error checking.
# ==> 2) Add bells & whistles.
