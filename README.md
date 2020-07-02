# ls-command-in-python

A program that works like the ls command.
Parameters can be given in any order.

1. The names are displayed without any parameter

  python3 ls.py folder_path

2. The -l option to run the "long" form of results output to stdout (file name, size, modification time in the form "yyyy-mm-dd HH: MM: SS", rights)

  python3 ls.py folder_path -l

3. The -L option causing each file to contain the name of its owner

  python3 ls.py folder_path -l -L
