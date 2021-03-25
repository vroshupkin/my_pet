import argparse
import os
import sys
import database


my_parser = argparse.ArgumentParser(description='Add word to vocabulary.db')
my_parser.add_argument('path',
                       metavar='path',
                       type=str,
                       help='the path to list')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))

# https://realpython.com/command-line-interfaces-python-argparse/#defining-mutually-exclusive-groups