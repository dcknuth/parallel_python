from time import time, sleep
from subprocess import Popen
from pathlib import Path
T1 = time()
infile = "inputd05.txt"

with open(infile) as f:
    ls = f.read().strip().split("\n")

# part two, What is the length of the shortest polymer you can produce by
#  removing all units of exactly one type and fully reacting the result?
poly = list(ls[0])
# How many different letter types do we have?
letters = set(list(ls[0].lower()))
# loop through and remove each
cmd = r'C:\Users\dave\AppData\Local\Programs\Python\Python39\python.exe'
script = "day05p.py"
for l in letters:
    arg_list = [cmd, script, l]
    print(*arg_list)
    Popen(arg_list)
print("Time to get all solutions started is", time()-T1)

num_files = 0
files = []
while num_files != len(letters):
    sleep(1)
    p = Path("./out")
    files = [x for x in p.iterdir()]
    num_files = len(files)
    print("files so far are:", *files)

# results have to be lower than this
lowest = len(poly)
for x in files:
    with open("./" + str(x)) as f:
        cur_len = int(f.read())
    if cur_len < lowest:
        lowest = cur_len

print("Final length is", lowest)
print("Time taken for part 2 was", time()-T1)
