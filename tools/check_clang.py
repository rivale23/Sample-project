#!/usr/bin/env python

import os
import subprocess
import argparse
import glob
from pathlib import Path
import sys


errors = []


def CheckClangInFiles(path, extension):
    total_errors = 0
    for filename in Path(path).rglob(extension):
        if(not("generated" in str(filename)) and not("build" in str(filename)) and not("tools" in str(filename)) and not("test" in str(filename))):
            print(filename)
            clang_format_program = ['clang-format',
                                    '--output-replacements-xml', str(filename)]
            output = subprocess.run(
                clang_format_program, stdout=subprocess.PIPE)
            errors_on_file = str(output.stdout).count('/replacement') - 1
            if(errors_on_file != 0):
                errors.append((filename, errors_on_file))
                total_errors += 1
    return total_errors


def main():
    path = project_dir = Path(__file__).resolve(
    ).parents[1]  # go to source sirectory

    errors_in_c_files = CheckClangInFiles(path, "*.c")
    errors_in_h_files = CheckClangInFiles(path, "*.h")

    total_errors = errors_in_c_files + errors_in_h_files

    if(total_errors > 1):
        print(errors)
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
