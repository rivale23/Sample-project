#!/usr/bin/env python

import os
import subprocess
from pathlib import Path
import sys
'''
function to check for specific string or condition in the commit message
'''


def CheckConditionalMessage(commit_message):
    out = True
    if(commit_message[0:6] != "Condition"):
        out = False
    return True


def main():
    git_log_command = ['git', 'log', '--pretty=oneline']
    git_log = subprocess.run(git_log_command, stdout=subprocess.PIPE)
    commit = str(git_log.stdout).split('\\n')[0]
    message = commit.split(' ')
    n_commits = 0
    if(len(message) > 1):
        commit_message = message[1]
        n_commits += 1
        commit_mesage_no_spaces = commit_message.replace(" ", "")
        if(commit_mesage_no_spaces.find("Merge") == 0 or commit_mesage_no_spaces.find("#") == 0):
            return 0
        if(CheckConditionalMessage(commit_mesage_no_spaces)):
            print("Error message")
            print(
                "The commit ", message[0], "is failing, which is ", n_commits, " commits behind")
            return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
