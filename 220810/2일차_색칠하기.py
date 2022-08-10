import sys
sys.stdin = open('색칠하기.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*10 for _ in range(10)]
    cnt = 0

    for i in range(N):
        st_c, st_r, en_c, en_r, color = map(int, input().split())

        for r in range(st_r, en_r+1):
            for c in range(st_c, en_c+1):
                arr[r][c] += color

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')