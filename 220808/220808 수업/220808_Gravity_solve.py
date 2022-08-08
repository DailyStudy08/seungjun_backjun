import sys
sys.stdin = open('input1.txt', 'r')

t = int(input())

for i in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_value = 0

    for j in range(n):
        cnt = 0
        for k in range(j+1, n):
            if arr[j] > arr[k]:
                cnt += 1
        if max_value < cnt:
            max_value = cnt

    print(f'#{i} {max_value}')