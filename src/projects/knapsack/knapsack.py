import sys

def knapsack(v, w, n, c):
    output = []
    myMatrix = [[0] * (c+1) for _ in range(n+1)]
    for i in range(1, n + 1): 
        for j in range(c + 1):
            if w[i - 1] > j:
                myMatrix[i][j] = myMatrix[i - 1][j]
            else: 
                myMatrix[i][j] = max(myMatrix[i - 1][j], myMatrix[i - 1][j - w[i - 1]] + v[i - 1])

    for i in range(n, 0, -1):
        if myMatrix[i][c] != myMatrix[i-1][c]:
            myIndex = i-1
            output.append(myIndex)
            c -= w[myIndex]

    return output

def main(data):
    while data:
        try:
            li = []
            for i in data.readline().split(): li.append(int(i))
            c, n, v, w = li[0], li[1], [], []
            for i in range(n):
                val_weight = list()
                for j in data.readline().split(): val_weight.append(int(j))
                v.append(val_weight[0])
                w.append(val_weight[1])
            myIndex = knapsack(v, w, n, c)
            myIndex=sorted(myIndex)
            print(len(myIndex))
            for i, j in enumerate(myIndex):
                print(j, end=" ")
            print()
        except IndexError:
            break

if __name__ == "__main__":
    main(sys.stdin)