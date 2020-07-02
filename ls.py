#!/usr/bin/python
import os
import sys
import datetime
import pwd

arg_num = len(sys.argv)
if arg_num > 4:
	print("Maksymalnie 3 argumenty.")
	sys.exit()

value = 0
files_c = list()

def files(path):
	for file in os.listdir(path):
		files_c.append(file)

def permRWX(octal):
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

def modTime(filename):
	time = os.path.getmtime(filename)
	return datetime.datetime.fromtimestamp(time).replace(microsecond=0)

i = 0

if arg_num == 1:
	path = "."
else:
	while i != arg_num:
		if sys.argv[i] == '-l':
			if value < 2:		
				value = 1
		elif sys.argv[i] == '-L':
			value = 2
		if os.path.exists(sys.argv[i]):
			path = sys.argv[i]
		i += 1
	if not os.path.isdir(path):
		sys.exit("Folder nie istnieje.")

files(path)
files_c.sort()
for file in files_c:
	if value == 0:
		print(file[:30])
	elif value > 0:
		new_p = "./" + path + "/" + file
		status = os.stat(new_p)
		size = os.path.getsize(new_p)
		perm = permRWX(oct(status.st_mode & 0o777)[2:])
		mtime = modTime(new_p)
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