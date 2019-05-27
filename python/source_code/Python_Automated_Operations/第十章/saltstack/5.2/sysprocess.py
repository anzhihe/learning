def syspro():
    '''
        return System process number
    '''
    import os
    grains = {}
    pids = []
    try:
        for subdir in os.listdir('/proc'):
            if subdir.isdigit():
                pids.append(subdir)
        strlist=len(pids)
    except Exception,e:
        strlist=str(e)

    grains['sysprocessnum'] = str(len(pids))
    return grains