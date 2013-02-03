import fileinput

for l in fileinput.input():
    print "line: ", l
