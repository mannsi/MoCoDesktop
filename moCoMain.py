__author__ = 'mannsi'

import argparse
import moCo.main


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', help='Path to dropbox folder')
parser.add_argument('-id', '--id', help='Computer id')
args = parser.parse_args()


def run():
    moCo.main.run(args.id, args.path)


if __name__ == "__main__":
    run()