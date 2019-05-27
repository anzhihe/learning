#!/usr/bin/env python
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user='root'
env.hosts=['192.168.1.21','192.168.1.22','192.168.1.23']
env.password='SKJh935yft#'


@task
@runs_once
def tar_task():
    with lcd("/data/logs"):
        local("tar -czf access.tar.gz access.log")
@task
def put_task():
    run("mkdir -p /data/logs")
    with cd("/data/logs"):
        with settings(warn_only=True):
            result = put("/data/logs/access.tar.gz", "/data/logs/access.tar.gz")
        if result.failed and not confirm("put file failed, Continue[Y/N]?"):
            abort("Aborting file put task!")

@task
def check_task():
    with settings(warn_only=True):
        lmd5=local("md5sum /data/logs/access.tar.gz",capture=True).split(' ')[0]
        rmd5=run("md5sum /data/logs/access.tar.gz").split(' ')[0]
    if lmd5==rmd5:
        print "OK"
    else:
        print "ERROR"

@task
def go():
    tar_task()
    put_task()
    check_task()
