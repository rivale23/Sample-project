#!/usr/bin/env python

import os
import subprocess
import argparse
import glob
from pathlib import Path
import sys

def main():
    print("applying clang on all sources(.c) and headers(.h) ...")
    for filename in Path('.').rglob('*.c'):
        if(str(filename).find("build")!=0 and str(filename).find("archive")!=0 and str(filename).find("extern")!=0 and not("cmocka" in str(filename)) ):
            clang_format_program = ['clang-format' ,'-i', str(filename)]
            output=subprocess.run(clang_format_program,stdout=subprocess.PIPE)

    for filename in Path('.').rglob('*.h'):
        if(str(filename).find("build")!=0 and str(filename).find("archive")!=0 and str(filename).find("extern")!=0 and not("cmocka" in str(filename)) ):
            clang_format_program = ['clang-format' ,'-i', str(filename)]
            output=subprocess.run(clang_format_program,stdout=subprocess.PIPE)

if __name__ == '__main__':
    sys.exit(main())