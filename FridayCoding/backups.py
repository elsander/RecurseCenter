#!/usr/bin/env python

import os
import sys
import pickle
import datetime

def CheckPath():
    if not os.path.exists('.vcs'):
        print "You must run backup from directory root."
        print "If you haven't already, run 'backup init' or go to directory root and try again."
        return 1
    else:
        return 0

def rm():
    ## remove everything in current directory but .vcs/
    for item in os.listdir('.'):
        if not item.startswith('.vcs'):
            os.system('rm -rf ' + item)

def readHEAD():
    ## read in HEAD file
    f = open('.vcs/HEAD', 'rb')
    head = pickle.load(f)
    f.close()
    return head

def readLOG():
    ## read in LOG file
    f = open('.vcs/LOG', 'rb')
    log = pickle.load(f)
    f.close()
    return log

def writeHEAD(head):
    ## write head to HEAD file
    f = open('.vcs/HEAD', 'w')
    pickle.dump(head, f)
    f.close()

def writeLOG(log):
    ## write log to LOG file
    f = open('.vcs/LOG', 'w')
    pickle.dump(log, f)
    f.close()    

#########################################################################
    
def Init():
    if os.path.exists('.vcs'):
        print "A repository has already been initialized here"
    else:
        ## Create directory to store snapshots
        os.mkdir('.vcs')
        ## create dictionary of current HEAD and checkout number
        head = dict()
        head['curr'] = 0 ## HEAD commit number
        head['num'] = 0 ## total number of commits
        writeHEAD(head)

        ## Create log file
        log = dict()
        writeLOG(log)
        print "vcs initialized"

def Commit(message):
    flag = CheckPath()
    if not flag:
        ## what is the total commit number right now?
        ## read in HEAD
        head = readHEAD()
        commitNum = head['num'] + 1
        old = head['curr']

        ## make new commit directory
        os.mkdir('.vcs/' + str(commitNum))
        
        ## copy everything but .vcs/ into the commit directory
        for item in os.listdir('.'):
            if not item.startswith('.vcs'):
                os.system('cp ' + item + ' -r .vcs/' + str(commitNum))

        ## update HEAD to new commit
        head['curr'] = commitNum
        head['num'] = commitNum
        writeHEAD(head)

        ## add new commit to log
        log = readLOG()
        if commitNum == 1:
            log['1'] = {'parent':None, 'date':datetime.date.today(),
                        'message':message}
        else:
            log[str(commitNum)] = {'parent':old, 'date':datetime.date.today(),
                                   'message':message}
        writeLOG(log)
            
        print "Commit " + str(commitNum) + ' completed'

## NOTE: you can currently branch by committing from an old commit
def Checkout(num):
    flag = CheckPath()
    if not flag:
        ## check that the specified commit exists!
        if not os.path.exists('.vcs/' + str(num)):
            print "The requested commit does not exist."
        
        ## otherwise, we can keep going
        else:
            ## remove everything in current directory but .vcs/
            rm()
            ## now put everything from specified commit into root directory
            os.system('cp .vcs/' + str(num) + '/. -r .')

            ## update HEAD
            head = readHEAD()
            head['curr'] = int(num)
            writeHEAD(head)
            
            print "Repository now at commit " + str(num)

def Latest():
    flag = CheckPath()
    if not flag:
        ## read in HEAD info
        head = readHEAD()
        latest = head['num']

        ## clear repo
        rm()
        ## put everything from latest commit into root directory
        os.system('cp .vcs/' + str(latest) + '/. -r .')

        ## update HEAD
        head['curr'] = latest
        writeHEAD(head)

        print "HEAD is now at commit " + str(latest)

def Current():
    flag = CheckPath()
    if not flag:
        ## read in HEAD info
        head = readHEAD()
        ## print current commit number
        print "HEAD is currently at commit " + str(head['curr'])

def Log():
    flag = CheckPath()
    if not flag:
        ## read in LOG and HEAD
        log = readLOG()
        head = readHEAD()

        commit = head['curr']
        while commit:
            ## print log date-time information in order
            print 'Commit ' + str(commit) + ': created ' + str(log[str(commit)]['date'])
            print '\t Commit Message: ' + log[str(commit)]['message']

            ## now move to ancestor of current commit
            commit = log[str(commit)]['parent']

def Diff(commit1, commit2):
    flag = CheckPath()
    if not flag:
        print "Unique to commit " + str(commit1) + ":"
        for item in os.listdir('.vcs/' + str(commit1)):
            if not os.path.isfile('.vcs/' + str(commit2) + '/' + item):
                if os.path.isdir('.vcs/' + str(commit1) + '/' + item):
                    print '\t' + item + '/'
                else:
                    print '\t' + item
        print "Unique to commit " + str(commit2) + ":"
        for item in os.listdir('.vcs/' + str(commit2)):
            if not os.path.isfile('.vcs/' + str(commit1) + '/' + item):
                if os.path.isdir('.vcs/' + str(commit2) + '/' + item):
                    print '\t' + item + '/'
                else:
                    print '\t' + item
        
## call from command line
if __name__ == "__main__":
    Command = sys.argv[1]
    if Command == 'init':
        Init()
    elif Command == 'commit':
        try:
            Commit(sys.argv[2])
        except IndexError:
            print 'Include a message to make a commit'
    elif Command == 'checkout':
        ## second argument is commit number
        Checkout(sys.argv[2])
    elif Command == 'latest':
        Latest()
    elif Command == 'current':
        Current()
    elif Command == 'log':
        Log()
    elif Command == 'diff':
        Diff(sys.argv[2], sys.argv[3])
