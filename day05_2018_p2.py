from time import time

DEBUG = 4
T1 = time()

infile = "inputd05.txt"

with open(infile) as f:
    ls = f.read().strip().split("\n")

# part two, What is the length of the shortest polymer you can produce by
#  removing all units of exactly one type and fully reacting the result?
poly = list(ls[0])
# results have to be lower than this
lowest = len(poly)
# How many different letter types do we have?
letters = set(list(ls[0].lower()))
# loop through and remove each
for l in letters:
    if DEBUG > 4:
        print("current l is", l)
    lcap = l.upper()
    current_poly = []
    for j in poly:
        if j != l and j != lcap:
            current_poly.append(j)
    if DEBUG > 4:
        print(current_poly)
    # Now react this poly and save the lowest result
    i = 0
    while i < len(current_poly):
        if i > 0:
            if current_poly[i-1].isupper():
                if current_poly[i].islower():
                    if current_poly[i] == current_poly[i-1].lower():
                        #remove both
                        del current_poly[i-1:i+1]
                        i = i-1
                        continue
            if current_poly[i-1].islower():
                if current_poly[i].isupper():
                    if current_poly[i] == current_poly[i-1].upper():
                        #remove both
                        del current_poly[i-1:i+1]
                        i = i-1
                        continue
        if i < len(current_poly)-2:
            if current_poly[i+1].isupper():
                if current_poly[i].islower():
                    if current_poly[i] == current_poly[i+1].lower():
                        #remove both
                        del current_poly[i:i+2]
                        continue
            if current_poly[i+1].islower():
                if current_poly[i].isupper():
                    if current_poly[i] == current_poly[i+1].upper():
                        #remove both
                        del current_poly[i:i+2]
                        continue
        i += 1
    if len(current_poly) < lowest:
        lowest = len(current_poly)

print("Final length is", lowest)

print("Time taken for part 2 was", time()-T1)
