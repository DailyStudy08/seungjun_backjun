import sys
sys.stdin = open('lnput.txt', 'r')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    one_cnt = 0

    bottom_row_lst = [0]*100

    for i in range(100):
        if arr[0][i] == 1:
            one_cnt += 1
            element = one_cnt
            bottom_row_lst[i] = element
        else:
            element = 0
            bottom_row_lst[i] = element

    # print(bottom_row_lst)

    lst = [0]*one_cnt

    dr = [1, 0, 0]
    dc = [0, -1, 1]
    d = 0
    r, c = 0, 0
    idx = -1
    for i in range(100):
        if arr[0][i] == 1:
            r = 1
            c = i
            count = 1
            idx += 1
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
                        count += 1
                        # print(r, c)

                    if r == 99:
                        lst[idx] = count
                        break

                    if arr[r+dr[d]][c+dc[d]] == 1 and d == 2:
                        r += dr[d]
                        c += dc[d]
                        count += 1
                        # print(r, c)
                    elif arr[r+dr[d]][c+dc[d]] == 1 and d == 1:
                        r += dr[d]
                        c += dc[d]
                        count += 1
                        # print(r, c)
    mn = 1000
    for i in lst:
        if mn > i:
            mn = i

    ans = bottom_row_lst.index(lst.index(mn)+1)
    print(f'#{tc} {ans}')
