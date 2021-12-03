import sys

def countingstars(floodLists):
    finalString = str()
    for i in range(len(floodLists)):
        finalString += f'Case {i+1}: {helper(floodLists[i])}\n'
    print(finalString)
    
def helper(myList):
    if not myList: return 0
    visited = myList.copy() 
    islands = 0
    stack = [] 
    for i in range(len(myList)):
        for j in range(len(myList[0])):
            if visited[i][j] != '9' and myList[i][j] == '-':
                islands += 1
                stack.append((i, j))
                while stack:
                    row, col = stack.pop() 
                    if myList[row][col] == '-' and visited[row][col] != '9': visited[row][col] = '9'        
                    if  row + 1 < len(myList) and myList[row + 1][col] == '-': stack.append((row + 1, col))
                    if row - 1 >= 0 and myList[row - 1][col] == '-': stack.append((row - 1, col))
                    if  col + 1 < len(myList[0]) and myList[row][col + 1] == '-': stack.append((row, col + 1))
                    if col - 1 >= 0 and myList[row][col - 1] == '-': stack.append((row, col - 1))
    return islands

def main(data):
    myStr = str()
    for i in data: myStr += i
    myList = []
    myStr = ''.join(i for i in myStr if not i.isdigit())
    b = myStr.strip().split("\n")
    anotherList = []
    for i in b:
        if i != " ":
            anotherList.append(list(i))
        if i == " ": 
            myList.append(anotherList)
            anotherList = []
            
    myList.append(anotherList)        
    countingstars(myList)
    
if __name__ == "__main__":
    main(sys.stdin)