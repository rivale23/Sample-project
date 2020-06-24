#!/usr/bin/env python

import os
import subprocess
import argparse
import glob
from pathlib import Path
from pathlib2 import Path
from shutil import copyfile
import sys

'''
this function checks out the warning file from master and
reads the warnings there
'''


def GetWarningsFromMaster(filepath):
    print("checking from master")
    # reads the file to get the number of warnigns from master
    warnings_on_master, warnings_master = CountNoOfWarnings(filepath)
    return warnings_on_master, warnings_master


def CountNoOfWarnings(out_warning_file):
    file = open(out_warning_file, 'r')
    lines = file.readlines()
    no_of_warnings = 0
    warnings = []
    delta_index = 20
    for line in lines:  # for every line it splits  the content using ""
        index_of_warning = line.find("warning:")
        if(index_of_warning != -1):
            filename = os.path.basename(line[0:index_of_warning])
            end_index = index_of_warning + len("warning:") + delta_index
            warnings.append(filename + line[index_of_warning:end_index])
            no_of_warnings += 1
    file.close()
    return no_of_warnings, set(warnings)


'''
writes the total number of warnings to the file
'''


def WriteWarningsOnFile(out_warning_file, no_warnings):
    file = open(out_warning_file, 'w')
    # writes the warnigns as "warning:#"
    file.write("THIS FILE IS OVERWRITTEN ON CI ON EVERY BUILD\n")
    file.write("warning:" + str(no_warnings) + "")
    file.close()


def main(number_warnings_from_master, warnings_from_master):
    # gets the path of the project folder
    project_dir = Path(__file__).resolve().parents[1]
    out_warning_file_sumary = os.path.join(
        project_dir, "temp.warnings")  # path for the output with the total number of warnings

    # compute the number of warnings on current branch
    number_warnings_on_current_branch, current_warnings = CountNoOfWarnings(
        out_warning_file_sumary)

    print("warnings on current branch=", number_warnings_on_current_branch)
    print("warnings on master=", number_warnings_from_master)

    if number_warnings_from_master < number_warnings_on_current_branch:
        print("ERROR: You have increased the number of warnings by",
              str(number_warnings_on_current_branch - number_warnings_from_master))
        print("Check the out.warnings file in integration/master and compare with your warnings")
        diff = current_warnings.difference(warnings_from_master)
        for warning in diff:
            print("new warning=", warning)
        return 1

    elif (number_warnings_from_master > number_warnings_on_current_branch):
        print("You have reduced the number of warnings by",
              str(number_warnings_from_master - number_warnings_on_current_branch))
        return 0
    else:
        return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('warningsfile', type=str,
                        help='file from artifac with the total warnings on master')
    args = parser.parse_args()
    file_exist = os.path.isfile(args.warningsfile)
    if(not file_exist):
        print("file not found")
        sys.exit(0)
    number_warnings_from_master, warnings_from_master = GetWarningsFromMaster(
        args.warningsfile)
    sys.exit(main(number_warnings_from_master, warnings_from_master))
