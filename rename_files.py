# -*- coding: utf-8 -*-
import os
import argparse

parser = argparse.ArgumentParser(description="Rename files from the given path")
parser.add_argument('-o','--old', help='This is old substring to be replaced',required=True)
parser.add_argument('-n','--new', help='This is new substring, which would replace old substring.',required=True)
parser.add_argument('-c','--capitalize', action="store_true", help='If passed, this argument will capitalize every first letter after a white space', default=False)
args = parser.parse_args()

def capitalize(s):
    return(' '.join(x.capitalize() for x in s.split(' ')))


print("where are the files you whish to rename?")
folder = raw_input("type the full folder path\n")

for file in os.listdir(folder):
    old_name = file
    new_name = old_name.replace(args.old, args.new)
    if args.capitalize:
        new_name = capitalize(new_name)

    os.rename(os.path.join(folder, old_name), os.path.join(folder, new_name))

