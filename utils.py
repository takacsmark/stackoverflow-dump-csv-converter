from typing import List, Dict
import sys
import re
import os.path
import subprocess
import json

from constants import *

def print_usage(message):
    """Prints script usage instructions
    """
    
    if message:
        print()
        print(message)

    print("""Usage:
    contverter [options] filename workdir [release]

    Options:
    -f, --force             Overwrite output CSV file if exists.
    -p, --progress-bar      Show progress bar. If the release argument is specified and a line_numbers entry with key release exists in `meta.py`, then the progress bar uses this entry to display progress. Otherwise the script will count the lines in the input file, which might take long. 

    Arguments:
    - filename              Name of the Stackverflow data file to be converted without extension. Value must be One of Badges, Comments, PostHistory, PostLinks, Posts, Tags, Users or Votes. 
    - workdir               Directory where the input file is located. The output directory will the same as workdir.
    - release               Release date of the dump file in YYYY_MM format (e.g. 2019_12).""")

    sys.exit(1)

def init_from_arguments(args: List):
    """Extracts options and arguments from command line arguments
    """

    # extracts options
    force_overwrite = False
    progress_bar = False

    while bool(re.match(r"^-.*", args[0])):
        if bool(re.match(r"^(-f|--force)", args[0])):
            force_overwrite = True
        elif bool(re.match(r"^(-p|--progress-bar)", args[0])):
            progress_bar = True
        else:
            print_usage("Error: Unkown option '{}'.\n".format(args[0]))

        args.pop(0)

    # extracts arguments
    len(args) < 2 and print_usage() #not enough arguments provided

    filename: str
    if args[0] in data_types:
        filename = args[0]  
    else:
        print("Error: Unkown data type '{}'.\n".format(args[0]))
        print_usage()

    workdir = args[1]
    if not os.path.isdir(workdir):
        sys.exit("Error: Working directory does not exist.")

    if not os.path.isfile(workdir + "/" + filename + ".xml"):
        sys.exit("Error: Input file does not exists at give path.")

    release = args[2] if len(args) == 3 else None #release is optional
    
    return force_overwrite, progress_bar, filename, workdir, release

def read_meta_from_file():
    """Reads meta information from meta file.
    """

    try:
        with open(meta_file_name, "r") as meta_file:
            return json.load(meta_file)
    except OSError:
        sys.exit("Could not open/read meta file: meta.json.")


def count_lines_in_file(workdir: str, filename: str):
    """Count lines in a file
    """
   
    print("Counting the number of lines in the input file. This may take several minutes.") 
    return int(re.search(r'\d+', subprocess.check_output(["wc", "-l", workdir + "/" + filename + ".xml"]).decode("utf-8")).group())


def update_meta_file(meta: Dict):
    """Updates meta information in meta file.
    """
    print("Updating meta file.")

    try:
        with open(meta_file_name, "w") as meta_file:
            json.dump(meta, meta_file)
    except OSError:
        sys.exit("Could not open/write meta file: meta.json.")


