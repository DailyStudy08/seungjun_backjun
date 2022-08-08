T = int(input())
test_num = 1
for i in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    s = f'#{test_num} '
    ans_lst = []
    index = 0
    for j in lst:
        cnt = 0
        for k in lst[index+1:]:
            if j <= k:
                cnt += 1
        ans_lst.append(N-1-index-cnt)
        index +=1
    max_arr = ans_lst[0]
    for j in ans_lst[1:]:
        if j >= max_arr:
            max_arr = j
    s += str(max_arr)
    print(s)
    test_num += 1