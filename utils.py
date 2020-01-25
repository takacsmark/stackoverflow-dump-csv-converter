from typing import List
import sys
import re
import os.path

data_types = ["Badges", "Comments", "PostHistory", "PostLinks", "Posts", "Tags", "Users", "Votes"]

def print_usage():
    """Prints script usage instructions
    """

    print("""Usage:
    contverter [options] dataset workdir [release]

    Options:
    -f, --force             Overwrite output CSV file if exists.
    -p, --progress-bar      Show progress bar. If the release argument is specified and a line_numbers entry with key release exists in `meta.py`, then the progress bar uses this entry to display progress. Otherwise the script will count the lines in the input file, which might take long. 

    Arguments:
    - dataset               Name of the Stackverflow dataset. One of Badges, Comments, PostHistory, PostLinks, Posts, Tags, Users or Votes. 
    - workdir               Directory where the input dataset is located. The output directory will the same as workdir.
    - release               Release version of the dataset in YYYY_MM format (e.g. 2018_12).""")

    sys.exit()

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
            print("Error: Unkown option '{}'.\n".format(args[0]))
            print_usage()

        args.pop(0)

    # extracts arguments
    len(args) < 2 and print_usage() #not enough arguments provided

    dataset: str
    if args[0] in data_types:
        dataset = args[0]  
    else:
        print("Error: Unkown data type '{}'.\n".format(args[0]))
        print_usage()

    workdir = args[1]
    if not os.path.isdir(workdir):
        sys.exit("Error: Working directory does not exist!")

    release = args[2] if len(args) == 3 else None #release is optional
    
    return force_overwrite, progress_bar, dataset, workdir, release
