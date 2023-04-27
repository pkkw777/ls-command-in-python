#!/usr/bin/python
import os
import sys
import datetime
import pwd

if len(sys.argv) > 4:
    print("Maksymalnie 3 argumenty.")
    sys.exit()

files_c = []

def list_files(path):
    return sorted(os.listdir(path))

def get_permissions(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    for perm in [int(n) for n in str(octal)]:
        for value, letter in value_letters:
            if perm >= value:
                result += letter
                perm -= value
            else:
                result += "-"
    return result

def get_modification_time(filename):
    time = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(time).replace(microsecond=0)

if len(sys.argv) == 1:
    path = "."
else:
    value = 0
    for i, arg in enumerate(sys.argv):
        if arg == '-l':
            if value < 2:		
                value = 1
        elif arg == '-L':
            value = 2
        elif os.path.exists(arg):
            path = arg
        if i == len(sys.argv)-1 and not os.path.isdir(path):
            sys.exit("Folder nie istnieje.")

for file in list_files(path):
    if value == 0:
        print(file[:30])
    else:
        new_p = os.path.join(path, file)
        status = os.stat(new_p)
        size = os.path.getsize(new_p)
        perm = get_permissions(oct(status.st_mode & 0o777)[2:])
        mtime = get_modification_time(new_p)
        own_name = pwd.getpwuid(status.st_uid).pw_name
        pattern = perm + " " + '{0:10d}'.format(size)[:10] + " " + '{}'.format(mtime) + " "
        if value == 2:
            if os.path.isdir(new_p):
                print("d" + pattern + own_name + " " + file[:30])
            else:
                print("-" + pattern + own_name + " " + file[:30])
        else:
            if os.path.isdir(new_p):
                print("d" + pattern + file[:30])
            else:
                print("-" + pattern + file[:30])
