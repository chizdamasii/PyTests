import sys
import itertools
f = open(sys.argv[1], 'r')
f = open('input.txt', 'r')

l = f.readline()[:-1].split(" ")
p1 = sorted(set([int(x) for x in f.readline().strip(' \n').split(" ")]))
p2 = sorted(set([int(x) for x in f.readline().strip(' \n').split(" ")]))
p3 = sorted(set([int(x) for x in f.readline().strip(' \n').split(" ")]))
common =list(set(p1).intersection(p2).difference(p3))
common= [a for a in common if (a>=1 and a<=500)]
result = 0

for i in range(0,len(common)+1):
    for l in list(itertools.combinations(common, i)):
        check = list(l)
        check.extend(p3)
        if all(check in p2 for check in p3):
            result+=1

print(result)