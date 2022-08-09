import sys
sys.stdin = open('sample_input(4).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    arr = [0] * (N-M+1)

    for i in range(N-M+1):
        sum = 0
        for j in range(M):
            sum += lst[i+j]
        arr[i] = sum

    mx = 0
    for i in range(len(arr)):
        if mx < arr[i]:
            mx = arr[i]

    mn = mx
    for j in range(len(arr)-1, -1, -1):
        if mn > arr[j]:
            mn = arr[j]
    # print(arr)
    print(f'#{tc} {mx-mn}')
