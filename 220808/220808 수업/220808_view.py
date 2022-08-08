import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    for i in range(2, N-2):
        mx = lst[i-2]
        for j in range(i-1, i+3):
            if i == j:
                continue
            if mx < lst[j]:
                mx = lst[j]
        if lst[i] > mx:
            cnt += (lst[i]-mx)

    print(f'#{tc} {cnt}')