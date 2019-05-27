import os,sys,commands

def Grains_openfile():
    '''
        return os max open file of grains value
    '''
    grains = {}

    #init default value
    _open_file=65536

    try:
        getulimit=commands.getstatusoutput('source /etc/profile;ulimit -n')
    except Exception,e:
        pass
    if getulimit[0]==0:
    	_open_file=int(getulimit[1])
    grains['max_open_file'] = _open_file
    return grains
