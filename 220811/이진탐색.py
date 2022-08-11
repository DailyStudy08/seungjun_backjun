import sys
sys.stdin = open('이진탐색.txt', 'r')

T = int(input())

def binary_search(pages, target):
    left = 1
    right = pages
    count = 1
    while left <= right:
        mid = int((left+right)/2)
        if target == mid:
            return count
        elif target > mid:
            left = mid
            count += 1
        elif target < mid:
            right = mid
            count += 1

for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    cnta = binary_search(P, A)
    cntb = binary_search(P, B)

    if cnta < cntb:
        ans = 'A'
    elif cnta > cntb:
        ans = 'B'
    elif cnta == cntb:
        ans = 0
    else:
        pass

    print(f'#{tc} {ans}')