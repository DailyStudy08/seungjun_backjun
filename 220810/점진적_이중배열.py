# lst = [[1],[2,3],[4,5,6]]

arr = []
N = int(input())

for i in range(1,N+1):
    arr.append(list(map(int, input().split()))[:i])
    print(arr)