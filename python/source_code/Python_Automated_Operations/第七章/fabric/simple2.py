#!/usr/bin/env python
from fabric.api import * 

env.user='root'
env.hosts=['192.168.1.21','192.168.1.22']
env.password="SKJh935yft#"

@runs_once
def input_raw():
    return prompt("please input directory name:",default="/home")

def worktask(dirname):
    run("ls -l "+dirname)

@task
def go():
    getdirname = input_raw()
    worktask(getdirname)
