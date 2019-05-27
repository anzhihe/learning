#!/bin/bash
# $Id: ha.sh,v 1.2 2005/04/21 23:24:26 oliver Exp $
# Copyright 2005 Oliver Beckstein
# Released under the GNU Public License
# Author of script granted permission for inclusion in ABS Guide.
# (Thank you!)

#----------------------------------------------------------------
# pseudo hash based on indirect parameter expansion
# API: access through functions:
# 
# create the hash:
#  
#      newhash Lovers
#
# add entries (note single quotes for spaces)
#    
#      addhash Lovers Tristan Isolde
#      addhash Lovers 'Romeo Montague' 'Juliet Capulet'
#
# access value by key
#
#      gethash Lovers Tristan   ---->  Isolde
#
# show all keys
#
#      keyshash Lovers         ----> 'Tristan'  'Romeo Montague'
#
#
# convention: instead of perls' foo{bar} = boing' syntax,
# use
#       '_foo_bar=boing' (two underscores, no spaces)
#
# 1) store key   in _NAME_keys[]
# 2) store value in _NAME_values[] using the same integer index
# The integer index for the last entry is _NAME_ptr
#
# NOTE: No error or sanity checks, just bare bones.


function _inihash () {
    # private function
    # call at the beginning of each procedure
    # defines: _keys _values _ptr
    #
    # usage: _inihash NAME
    local name=$1
    _keys=_${name}_keys
    _values=_${name}_values
    _ptr=_${name}_ptr
}

function newhash () {
    # usage: newhash NAME
    #        NAME should not contain spaces or '.';
    #        actually: it must be a legal name for a bash variable
    # We rely on bash automatically recognising arrays.
    local name=$1 
    local _keys _values _ptr
    _inihash ${name}
    eval ${_ptr}=0
}


function addhash () {
    # usage: addhash NAME KEY 'VALUE with spaces'
    #        arguments with spaces need to be quoted with single quotes ''
    local name=$1 k="$2" v="$3" 
    local _keys _values _ptr
    _inihash ${name}

    #echo "DEBUG(addhash): ${_ptr}=${!_ptr}"

    eval let ${_ptr}=${_ptr}+1
    eval "$_keys[${!_ptr}]=\"${k}\""
    eval "$_values[${!_ptr}]=\"${v}\""
}

function gethash () {
    # usage: gethash NAME KEY
    #        returns boing
    #        ERR=0 if entry found, 1 otherwise
    # Thats not a proper hash---we simply linearly search through the keys
    local name=$1 key="$2" 
    local _keys _values _ptr 
    local k v i found h
    _inihash ${name}
    
    # _ptr holds the highest index in the hash
    found=0

    for i in $(seq 1 ${!_ptr}); do
	h="\${${_keys}[${i}]}"  # safer to do it in two steps
	eval k=${h}             # (especially when quoting for spaces)
	if [ "${k}" = "${key}" ]; then found=1; break; fi
    done;

    [ ${found} = 0 ] && return 1;
    # else: i is the index that matches the key
    h="\${${_values}[${i}]}"
    eval echo "${h}"
    return 0;	
}

function keyshash () {
    # usage: keyshash NAME
    # returns list of all keys defined for hash name
    local name=$1 key="$2" 
    local _keys _values _ptr 
    local k i h
    _inihash ${name}
    
    # _ptr holds the highest index in the hash
    for i in $(seq 1 ${!_ptr}); do
	h="\${${_keys}[${i}]}"   # Safer to do it in two steps
	eval k=${h}              # (especially when quoting for spaces)
	echo -n "'${k}' "
    done;
}


# --------------------------------------------------------------------

# Now, let's test it.
# (Per comments at the beginning of the script.)
newhash Lovers
addhash Lovers Tristan Isolde
addhash Lovers 'Romeo Montague' 'Juliet Capulet'

# Output results.
echo
gethash Lovers Tristan      # Isolde
echo
keyshash Lovers             # 'Tristan' 'Romeo Montague'
echo; echo


exit 0

# Exercise: Add error checks to the functions.
