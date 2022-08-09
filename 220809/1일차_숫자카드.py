import sys
sys.stdin = open('sample_input(3).txt', 'r')

T = int(input())  #3

for tc in range(1, T+1):
    num = int(input())
    counts = [0] * 10

    card = list(map(int, input()))

    for i in card:
        counts[i] += 1

    mx = counts[0]
    ind = 0
    for i in range(0, len(counts)):
        if mx <= counts[i]:
            mx = counts[i]
            ind = i

    print(f'#{tc} {ind} {mx}')