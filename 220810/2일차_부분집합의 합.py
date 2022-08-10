# import sys
# sys.stdin = open('부분집합의_합.txt', 'r')

arr = [1,2,3,4,5,6,7,8,9,10,11,12]

def len__(arr):
    len = 0
    for _ in arr:
        len += 1
    return len

def sum__(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    len2 = len__(arr)

    for i in range(1<<len2):
        temp = []
        for j in range(len2):
            if i & (1<<j):
                temp.append(arr[j])
        len1, sum1 = len(temp), sum(temp)
        # print(temp, len1, sum1)
        if len1 == N and sum1 == K:
            cnt += 1
    print(f'#{tc} {cnt}')