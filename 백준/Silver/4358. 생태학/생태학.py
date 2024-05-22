import sys
from collections import Counter

treeName = []
while True:
    
    inputTree = sys.stdin.readline().strip()

    if not inputTree:
        break
    treeName.append(inputTree)


treeName.sort()
c = Counter(treeName)


percents = list(c.values())
tmp = set(treeName)
tmp = list(tmp)
tmp.sort()
for i in range(len(percents)):
    print(tmp[i] + " %0.4f" % (percents[i] / len(treeName) * 100))
    