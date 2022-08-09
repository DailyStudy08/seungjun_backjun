import sys
sys.stdin = open('sample_input(2).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    # lst = [0]*(N+1)
    charger = list(map(int, input().split()))
    # [1, 3, 5, 7, 9]

    now = 0
    battery = K
    c_idx = 1 #충전소 다음 인덱스
    cnt = 0 #충전 횟수

    while now < N-1:
        now += 1
        battery -= 1

        if now in charger:

            if battery < charger[c_idx]-now or (c_idx == M-1 and battery < N-now):
                battery = K
                cnt += 1

            if c_idx < M-1:
                c_idx += 1

        if not battery:
            cnt = 0
            break

    print(f'#{tc} {cnt}')
