#!/usr/bin/env python
"""
%HERE%
"""

__date_ = "%DATE%"
__author__ = "%USER%"
__email__ = "%MAIL%"
__license__ = "%LICENSE%"

# imports
import sys
import csv
import time
import errno
from argparse import ArgumentParser, RawTextHelpFormatter

parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
parser.add_argument("-v",
                    "--verbose",
                    dest="verbose",
                    action="store_true",
                    default=False,
                    help="Be loud!")
parser.add_argument("-d",
                    "--delimiter",
                    dest="delimiter",
                    default="\t",
                    help="Delimiter for reading, defaults to \\t")

try:
    options = parser.parse_args()
except Exception, e:
    parser.print_help()

# redefine a functions for writing to stdout and stderr to save some writting
syserr = sys.stderr.write
sysout = sys.stdout.write


def main():
    """Main logic of the script"""
    try:
        for row in csv.reader(sys.stdin, delimiter=options.delimiter):
            pass
    except IOError as e:
        if e.errno == errno.EPIPE:
            pass

if __name__ == '__main__':
    try:
        if options.verbose:
            start_time = time.time()
            start_date = time.strftime("%d-%m-%Y at %H:%M:%S")
            syserr("############## Started script on %s ##############\n" % start_date)
        main()
        if options.verbose:
            syserr("### Successfully finished in %i seconds, on %s ###\n" % (time.time() - start_time, time.strftime("%d-%m-%Y at %H:%M:%S")))
    except KeyboardInterrupt:
        syserr("Interrupted by user after %i seconds!\n" % (time.time() - start_time))
        sys.exit(-1)