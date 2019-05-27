#!/usr/bin/env python
from fabric.api import *

env.user='root'
env.hosts=['192.168.1.21','192.168.1.22']
env.password='SKJh935yft#'

@runs_once
def local_task():
    local("uname -a")

def remote_task():
    with cd("/data/logs"):
        run("ls -l")
