__author__ = 'mannsi'

import argparse
import moCo.main


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', help='Path to dropbox folder')
args = parser.parse_args()


def run():
    moCo.main.run(args.path)