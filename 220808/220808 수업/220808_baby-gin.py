T = int(input())

for tc in range(1, T+1):
    lst = [0]*10
    numbers = list(map(int, input()))

    for i in numbers:
        lst[i] += 1

    ans = 0
    for j in range(len(lst)):
        # run
        if lst[j] >= 1 and lst[j+1] >=1 and lst[j+2]>=1:
            ans += 1
            lst[j] -= 1
            lst[j+1] -= 1
            lst[j+2] -= 1
        # triplet
        elif lst[j] >= 3:
            ans += 1
            lst[j] -= 3
        else:
            continue

    if ans == 2:
        print(True)
    else:
        print(False)