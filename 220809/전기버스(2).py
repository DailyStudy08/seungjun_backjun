import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    battery = list(map(int, input().split()))

    stations = [0]*N
    for idx in battery:
        stations[idx] = 1

    cnt = 0
    position = 0

    while True:
        position += K
        if position >= N:
            break

        for i in range(position, position-K, -1):
            if stations[i] == 1:
                cnt += 1
                position = i
                break
        else:
            cnt = 0
            break

    print(f'#{tc} {cnt}')