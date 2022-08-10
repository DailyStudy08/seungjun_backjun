import sys
sys.stdin = open('input3.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())   # 배열 길이
    arr = [[0 for j in range(n)] for i in range(n)]
    num = 1
    st = 0

    def make_outer(arr, st, length, num):       # st: 시작 인덱스, length  : n, num: 시작인덱스의 시작 숫자
        last = st+length-1   #마지막 인덱스
        for c in range(st, last+1):
            arr[st][c] = num
            num += 1
        for r in range(st+1, last+1):
            arr[r][last] = num
            num += 1
        for c in range(last-1, st-1, -1):
            arr[last][c] = num
            num += 1
        for l in range(last-1, st, -1):
            arr[l][st] = num
            num += 1
        return num

    while n > 0:
        num = make_outer(arr, st, n, num)
        n -= 2
        st += 1

    print(f'#{tc}')
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=' ')
        print()