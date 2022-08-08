import sys
# input = sys.stdin.readline
sys.stdin = open('input1.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_height = numbers[0]
    for i in range(1, len(numbers)):
        if max_height <= numbers[i]:
            max_height = numbers[i]

    final_list = [[0]*max_height for _ in range(N)]

    for n in range(N):
        for s in range(numbers[n]):
            final_list[n][s] = 1

    max_result = 0
    for n in range(N):
        for s in range(max_height-1, -1, -1):
            cnt = 0
            if final_list[n][s] == 1:
                for k in range(n+1, N):
                    if final_list[k][s] == 0:
                        cnt += 1
                    if max_result < cnt:
                        max_result = cnt
    print(f'#{tc} {max_result}')