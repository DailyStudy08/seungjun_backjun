import sys
sys.stdin = open('이진탐색.txt', 'r')

def binary(P, A, B):
    left_a, left_b = 1, 1
    success_a, success_b = False, False
    right_a, right_b = P, P

    while True:
        mid_a = (left_a + right_a - 1) // 2
        if A == mid_a:
            success_a = True
        elif A < mid_a:
            right_a = mid_a - 1
            mid_a = (left_a + right_a - 1) // 2
        elif A > mid_a:
            left_a = mid_a + 1
            mid_a = (left_a + right_a - 1) // 2


        mid_b = (left_b + right_b - 1) // 2
        if B == mid_b:
            success_b = True
        elif B < mid_b:
            right_b = mid_b - 1
        elif B > mid_b:
            left_b = mid_b + 1


        if success_a == True and success_b == True:
            return 0
        elif success_a == True and success_b == False:
            return 'A'
        elif success_a == False and success_b == True:
            return 'B'
        else:
            continue

T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    ans = binary(P, A, B)
    print(f'#{tc} {ans}')