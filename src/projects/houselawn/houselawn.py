import sys

def houseLawn(num, size, m, l):
    mowerList = []
    for i in range(num):  
        v1,v2,v3,v4 = m[i].split(',')
        v1, v2, v3, v4 = map(int, (v1, v2, v3, v4))
        time = (10080 // (v3 + v4)) * v3 + min(10080 % (v3 + v4), v3)
        if size <= time * v2 and v2 * v3 * 10080 >= size * (v3 + v4):
            mowerList.append((v1, i, l[i]))
    if len(mowerList) == 0:
        print('no such mower')
    else:
        mowerList = sorted(mowerList)
        for v1, i, l[i] in mowerList:
            if v1 == mowerList[0][0]: print(l[i])

def main(data):
    line = data.readlines()
    result = []
    values = []
    m = []
    l = []
    for i in line: result.append(i.strip().split(",", 1))
    for i in result[0]: values.append(i.split())
    s, n = int(values[0][0]), int(values[0][1])
    result = result[1::]
    for i in result: l.append(i[0])
    for i in result: m.append(i[1])
    houseLawn(n,s,m,l)

if __name__ == "__main__":
    main(sys.stdin)