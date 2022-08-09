import sys
sys.stdin = open('input(5).txt', 'r')

T = 10
for tc in range(1, T+1):
    dump = int(input())
    box_lst = list(map(int, input().split()))
    while dump > 0:
        max_value, min_value = box_lst[0], box_lst[0]
        max_idx, min_idx = 0
        min_value = box_lst[0]
        min_idx = 0

        for i in range(len(box_lst)):
            if box_lst[i] > max_value:
                max_value = box_lst[i]
                max_idx = i
            elif box_lst[i] < min_value:
                min_value = box_lst[i]
                min_idx = i

        box_lst[max_idx] -= 1
        box_lst[min_idx] += 1

        dump -= 1

    max_value, min_value = box_lst[0], box_lst[0]

    for i in range(len(box_lst)):
        if box_lst[i] > max_value:
            max_value = box_lst[i]
        elif box_lst[i] < min_value:
            min_value = box_lst[i]

    if max_value - min_value >= 0:
        print(f'#{tc} {max_value - min_value}')
