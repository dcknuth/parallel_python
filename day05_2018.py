from time import time

DEBUG = 5
T1 = time()

infile = "inputd05.txt"

with open(infile) as f:
    ls = f.read().strip().split("\n")

# part one, How many units remain after fully reacting the polymer you
#  scanned?
# Just try with a list and brute force?
poly = list(ls[0])
done = False
while not done:
    done = True
    for i, x in enumerate(poly):
        if i < len(poly) - 1 and x.islower():
            if poly[i+1].isupper():
                if x == poly[i+1].lower():
                    poly = poly[:i] + poly[i+2:]
                    done = False
                    break
        elif i < len(poly) -1:
            if poly[i+1].islower():
                if x == poly[i+1].upper():
                    poly = poly[:i] + poly[i+2:]
                    done = False
                    break
print("Final length is", len(poly))

print("Time taken for part 1 was", time()-T1)
