import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # arr = [[1,2,3,4,5],
    #        [6,7,8,9,10],
    #        [11,12,13,14,15],
    #        [16,17,18,19,20],
    #        [21,22,23,24,25]]

    lst = [[0]*N for _ in range(N)]

    def abs_sum(arr, i, j):
        sum = 0
        dy = [1,-1,0,0]
        dx = [0,0,1,-1]
        for _ in range(4):
            ny = i + dy[_]
            nx = j + dx[_]
            if 0 <= ny < 5 and 0 <= nx < 5:
                sum += abs(arr[ny][nx] - arr[i][j])
        lst[i][j] = sum

    for i in range(5):
        for j in range(5):
            abs_sum(arr,i,j)

    ans = 0
    for i in range(5):
        for j in range(5):
            ans += lst[i][j]

    print(f'#{tc} {ans}')