# Parallel Python
Some attempts at parallelizing things in Python

I did a [walk through](aoc_walkthrough.md) of a day of Advent of Code and then thought I would come back and parallelize it. Since this solution takes about a minute and would need 26 of them, it should work well because the only thing that would need to be different to each of the 26 runs would be which letter to strip out, which fits nicely as a command-line parameter. Even on Windows where starting another process might take a second, this solution runs long enough to be worth it. The first thing to figure out is how to run another process, feeding it some input somehow and then not waiting for that to finish to be able to start another with a little different input. Here are some ways to launch a separate process from Python:
```
import os
# Run a command and wait for it to finish
cmd = 'notepad'
return_val = os.system(cmd)
print("Returned", return_val)

# Run and don't wait to finish
start_dir = r'"C:\Users\dave\Documents\Python Scripts\aoc2018"'
cmd = 'start /d ' + start_dir + r' C:\Windows\System32\notepad.exe'
os.system(cmd)
print("Back to Python")

# the os.system call shouldn't be used anymore. Use subprocess instead
import subprocess
# Again, waits for return value
cmd = 'notepad'
subprocess.run(cmd)
print("Back to Python")

# Don't wait for return
cmd = r'C:\Users\dave\AppData\Local\Programs\Python\Python39\python.exe'
script = "C:/Users/dave/Documents/Python Scripts/aoc2018/test.py"
arg_list = [cmd, script]
print(*arg_list)
subprocess.Popen(arg_list)
print("Back to Python")
```

It took 2 minutes to find the first example above and then much longer to get to the last example of the four, which is probably more like what we would want. It seems doing this is not very popular from Python on Windows. The item to learn was that subprocess.run() will always wait for what you start to complete and subprocess.Popen() will not wait by default. Now that we can start a bunch of separate Python scripts, the plan is to re-write the brute force solution a bit to only need the letter to work on for a case. It will also write the length found to a file. Then the main Python script will start all 26 solutions and loop/wait until all the output files appear. Then it will read them and grab the lowest. [This](day05p.py) is the parallel re-write of the brute force solution.

It now will strip out the letter passed in on the command line and write its output to a file. This solution needs [a wrapper](day05p_wrap.py) to run for each letter.

It took 0.05 seconds to kick off all the scripts and about 67 seconds to get the final result. Since getting one result took about 52 seconds, this is pretty good and actually better scaling than the 16 real cores in the system and removing one letter would predict, so we are even getting a little virtual threading benefit. There is a module to help you do this automatically instead of via file IO, but this was easy to understand and follow. Also, since solid state drives, the penalty to doing this type of split and aggregation through files has come way down.

I used the same approach in the Teach Yourself Python class in [lesson 14 part 2](https://github.com/dcknuth/teach_yourself_python/blob/main/lesson14p2.md) I did eventually decide to use the built-in support way of parallelizing Python [here](https://github.com/dcknuth/aoc2024/blob/main/day06v2.py) in [day 6 of 2024 AoC](https://github.com/dcknuth/aoc2024/blob/main/day06v2.py). Again, got good virtual multi-threading speed gains, 82 to 4 seconds. This last is probably the recommended way to parallelize Python, but the other is easy to understand and versatile