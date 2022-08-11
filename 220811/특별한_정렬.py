import sys
sys.stdin = open('특별한 정렬.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    arr = [0]*len(lst)
    cnt = 0

    while cnt < 10:
        mx = 0
        mn = 100
        for i in range(len(lst)):
            if mx < lst[i]:
                mx = lst[i]
            if mn > lst[i]:
                mn = lst[i]

        i = 0
        while True:
            if i%2==0 and arr[i]==0:
                arr[i] = mx
            elif i%2==1 and arr[i]==0:
                arr[i] = mn
                cnt += 2
                break
            i += 1

        lst.remove(mx)
        lst.remove(mn)

    print(f'#{tc}', end=' ')
    for i in arr[:10]:
        print(i, end=' ')
    print()