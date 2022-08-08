import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    final_list = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(numbers[i]):
            final_list[i][j] = 1

    max_v = 0
    for n in range(N):
        for m in range(M):
            cnt = 0
            if final_list[n][m] == 1:
                for k in range(n+1, N):
                    if final_list[k][m] == 0:
                        cnt += 1
                if cnt > max_v:
                    max_v = cnt

    print(f'#{tc} {max_v}')