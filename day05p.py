import sys
infile = "inputd05.txt"
out_dir = "out/"
with open(infile) as f:
    ls = f.read().strip().split("\n")

# part one, How many units remain after reacting the polymer
l = sys.argv[1].strip()
lcap = l.swapcase()
poly = []
for j in list(ls[0]):
    if j != l and j != lcap:
        poly.append(j)

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
out_file = out_dir + l + ".txt"
f = open(out_file, "w")
f.write(str(len(poly)))
f.close()
