import sys
from collections import defaultdict

def torn(res, dest, myGraph, v):
        while res and dest != res[0][0]:
            s, r = res.pop(0)
            if s not in v:
                v.add(s)
                for i in myGraph[s] - v:
                    res.append((i, r + [i]))

def main(data):
    myGraph, myList, line, res = defaultdict(set), list(), data.readlines(), list()

    for i in line: 
        myList.append(i.strip().split())

    number, start, dest = int(myList[0][0]), myList[-1][0], myList[-1][-1]
    myList.pop(0)
    myList.pop(-1)

    for i in range(number):
        for j in myList: 
            for sub in j:    
                myGraph[j[0] ].add(sub)
                myGraph[sub].add(j[0])

        for i in myGraph[start]: res.append((i, [start,i]))
        torn(res, dest, myGraph, set([start]))

    if res: 
        print(" ".join(res[0][1]))
    else: 
        print("no route found")   
        
if __name__ == "__main__":
    main(sys.stdin)