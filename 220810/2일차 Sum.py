import sys
sys.stdin = open('sum_input.txt', 'r')

for _ in range(1, 11):
    tc = int(input())

    lst = [list(map(int, input().split())) for _ in range(100)]

    mx = 0
    for i in range(100):
        sm = 0
        for j in range(100):
            sm += lst[i][j]
        if mx < sm:
            mx = sm

    for i in range(100):
        sm = 0
        for j in range(100):
            sm += lst[j][i]
        if mx < sm:
            mx = sm

    sm = 0
    for i in range(100):
        sm += lst[i][100-1-i]
    if mx < sm:
        mx = sm

    sm = 0
    for i in range(100):
        sm += lst[i][i]
    if mx < sm:
        mx = sm

    print(f'#{tc} {mx}')