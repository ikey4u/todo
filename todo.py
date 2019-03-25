#! /usr/bin/env python3
#! -*- coding:utf-8 -*-
import argparse
import json
import os
import sys
import time

todopath = "$HOME/.todo.json"
def showtodo(todopath):
    todopath = os.path.expandvars(todopath)
    if(not os.path.exists(todopath)):
        print("No todo file found, please add at least one task!")
        sys.exit(1)
    with open(todopath,'r') as ftodo:
        task = json.load(ftodo)
        for tid in sorted(task.keys(),key = lambda k : int(k)):
            print("{0} ⇒ {1}".format(tid,task[tid]['title']))
            print("\t○ Status: {0}".format(task[tid]['status']))
            if(task[tid]['desc']):
                print('\t○ Description: {0}'.format(task[tid]['desc']))
            if(task[tid]['date']):
                print('\t○ Since: {0}'.format(task[tid]['date']))

if __name__ == "__main__":
    if(len(sys.argv) <= 1):
        showtodo(todopath)
        sys.exit(0)
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a","--add",nargs = '+',
            help = "Add a task,the task format is : title @ [description]")
    group.add_argument("-d","--delete",nargs = '+',help = "Delete a task")
    group.add_argument("-c","--change",metavar = ("ID","KEY","VAL"),
            nargs = 3,
            help = "Update a task,change is one keyword from [title|status|desc|date]")
    group.add_argument("-m","--mark",
            metavar = ("ID","STATUS"),
            nargs = 2,
            help = "Mark if a task is finished or not")
    args = parser.parse_args()

    if(not os.path.exists(todopath)):
        task = dict()
        with open(todopath,'w') as _:
            json.dump(task,_)

    with open(todopath,'r') as ftodo:
        task = json.load(ftodo)

    if(args.add):
        args.add = ''.join(args.add)
        if('@' not in args.add):
            atask = [args.add] + ['']
        else:
            atask = args.add.split('@') + ['']* (2 - len(args.add))
        adddate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        dtask = {'title':atask[0],'desc':atask[1],'status':'✗','date':adddate}
        task[str(len(task) + 1)] = dtask

    if(args.mark):
        tid,status = args.mark[0],args.mark[1]
        if(tid not in task.keys()):
            print("Task ID not found!")
        else:
            if(status == '1'):
                task[tid]['status'] = '✓'
            else:
                task[tid]['status'] = '✗'

    if(args.change):
        tid,key,val = args.change[0],args.change[1],args.change[2]
        if(key == 'status'):
            if(val == '1'):
                val = '✓'
            else:
                val = '✗'
        if(tid in task.keys()):
            task[tid][key] = val
        else:
            print("Task ID not found!")

    if(args.delete):
        for tid in args.delete:
            if(tid in task.keys()):
                del task[tid]

    #Rearrange todo ID
    taskids = sorted(task.keys(),key = lambda x : int(x))
    sortids = [str(i) for i in range(1,len(task) + 1)]
    for taskid,sortid in zip(taskids,sortids):
        task[sortid] = task[taskid]
        if(int(taskid) != int(sortid)):
            del task[taskid]

    with open(todopath,'w') as _:
        json.dump(task,_)
