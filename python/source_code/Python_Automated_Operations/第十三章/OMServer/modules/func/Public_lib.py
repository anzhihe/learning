import sys
import xmlrpclib
import func.overlord.client as fc

def target_host(hosts,target_type='HN'):
    target_string = ""
    hosts_string = ""
    for hrow in hosts.split(','):
        if target_type=="HN":
            hosts_string += hrow.split('*')[1]+";"
        elif target_type=="IP":
            hosts_string += hrow.split('*')[0]+";"
    target_string=hosts_string[0:len(hosts_string)-1]
    return target_string