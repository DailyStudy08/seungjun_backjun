import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # arr = [1, 2, 3, 4, 5, -5, -9, -12, -10, -11]
    # arr = [1,3,5,8]
    arr = list(map(int, input().split()))
    n = len(arr)    # n : 원소의 개수(4개)

    lst = []
    for i in range(1<<n):    # 1<<n : 부분 집합의 개수
        temp = []    # temp : 부분 집합을 저장할 임시 리스트 초기화
        for j in range(n):    # 원소의 수만큼 비트를 비교함
            if i&(1<<j):  #i의 j번째 비트가 1이면 True
                temp.append(arr[j])    # 비트가 1에 해당하는 원소를 부분 집합 리스트에 추가
        #부분 집합 출력
        lst.append(temp)

    zero_lst = [0]*(len(lst))

    for j in range(len(lst)):
        sum = 0
        for k in range(len(lst[j])):
            sum += lst[j][k]
        zero_lst[j] = sum

    # print(lst)
    # print(zero_lst)
    answer = []
    for l in range(1, len(zero_lst)):   # 공집합은 제외해야함
        if zero_lst[l] == 0:
            # answer.append(lst[l])
            print(f'#{tc} 1')
            break
    else:
        print(f'#{tc} 0')
    # print(answer)
