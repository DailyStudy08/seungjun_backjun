import sys
sys.stdin = open('input.txt','r')

def fucku(i, j):

    total = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            lst = []
            # 십자가 모양
            lst.append(arr[i][j])
            lst.append(arr[i][j-1])
            lst.append(arr[i][j+1])
            lst.append(arr[i-1][j])
            lst.append(arr[i+1][j])

            # 십자가에서 작은거 빼기
            lst.remove(min(lst))

            # 4개 합을 total에 넣기
            total.append(sum(lst))

    return max(total)

def dfs(i, j):
    global mx_lst
    stack = []
    stack.append((i, j))

    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, 1]




N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
sr, sc = 1, 1
#fuck you
result = fucku(sr, sc)

mx_lst = []
for i in range(N):
    for j in range(M):
        dfs(i, j)