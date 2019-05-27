import os,sys,commands

def NginxGrains():
    '''
        return Nginx config grains value
    '''
    grains = {}
    max_open_file=65536
    #Worker_info={'cpus2':'01 10','cpus4':'1000 0100 0010 0001','cpus8':'10000000 01000000 00100000 00010000 00001000 00000100 00000010 00000001'}
    try:
        getulimit=commands.getstatusoutput('source /etc/profile;ulimit -n')
    except Exception,e:
        pass
    if getulimit[0]==0:
    	max_open_file=int(getulimit[1])
    grains['max_open_file'] = max_open_file
    return grains
