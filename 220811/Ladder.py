import sys
sys.stdin = open('Ladder.txt', 'r')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    dr = [1, 0, 0]
    dc = [0, -1, 1]
    d = 0
    r, c = 0, 0
    for i in range(100):
        if arr[0][i] == 1:
            r = 0
            c = i
            while True:  # r < 10은 일단 뺏음 ( 점검 )
                if arr[r][c] == 1:
                    if c+dc[1] >= 0 and arr[r+dr[1]][c+dc[1]] == 1 and d != 2:
                        d = 1
                    elif c+dc[2] <= 99 and arr[r+dr[2]][c+dc[2]] == 1 and d != 1:
                        d = 2
                    elif c == 0 or c == 99 or arr[r+dr[d]][c+dc[d]] == 0 :
                        d = 0

                    if (arr[r+dr[d]][c+dc[d]] == 1 or arr[r+dr[d]][c+dc[d]] == 2) and d == 0:
                        r += dr[d]
                        c += dc[d]
                        # print(r, c)

                    if r == 99:
                        if arr[99][c] == 2:
                            print(f'#{tc} {i}')
                        break

                    if arr[r+dr[d]][c+dc[d]] == 1 and d == 2:
                        r += dr[d]
                        c += dc[d]
                        # print(r, c)
                    elif arr[r+dr[d]][c+dc[d]] == 1 and d == 1:
                        r += dr[d]
                        c += dc[d]
                        # print(r, c)
