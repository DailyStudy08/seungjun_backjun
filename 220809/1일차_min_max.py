import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    num = int(input())

    lst = list(map(int, input().split()))

    mx = lst[0]
    for i in range(1, num):
        if mx < lst[i]:
            mx = lst[i]

    mn = lst[0]
    for i in range(1, num):
        if mn > lst[i]:
            mn = lst[i]

    diff = mx - mn

    print(f'#{tc} {diff}')