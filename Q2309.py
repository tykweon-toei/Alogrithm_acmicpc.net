# Question : https://acmicpc.net/problem/2309
# Author : tykweon.toei
# memory : 9084 KB
# time : 80 ms

def identify(numList):
    value = sum(numList, 0)
    for i in range(0, 9):
        total1 = int(value) - numList[i]
        for j in range(i+1, 9):
            total2 = total1 - numList[j]
            if (total2 == 100):
                del numList[j]
                del numList[i]
                return numList

if(__name__=="__main__"):

    numList = [int(input()) for i in range(9)]
    numList.sort()
    ans = identify(numList)
    for m in ans:
        print(m)
