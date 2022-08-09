arr = [2, 4, 1, 7, 6, 2, 7, 8, 3, 1, 6]


def Counting(arr):
    # arr의 길이 구하기
    len = 0
    for i in arr:
        len += 1
    # 최댓값 구하기
    mx = arr[0]
    for i in range(len):
        if mx < arr[i]:
            mx = arr[i]
    # 카운트 배열을 0배열로 초기화(숫자마다 빈도수를 구하기 위해서)
    counts = [0] * (mx + 1)
    # 카운트 배열에 1씩 더해서 빈도수 구하기
    for i in range(0, len):
        counts[arr[i]] += 1
    # 카운트 배열 길이 구하기
    len_cnt = 0
    for i in counts:
        len_cnt += 1
    # 카운트 배열 누적합 만들기
    for i in range(1, len_cnt):
        counts[i] += counts[i - 1]
    # 임시 정렬 배열 초기화
    temp = [0] * len
    # 뒤에서부터 하나씩 빼기 위해서 정렬할 배열의 인덱스를 뒤에서 부터 뽑고, 새로운 인덱스에 정렬
    for i in range(len - 1, -1, -1):
        counts[arr[i]] -= 1
        temp[counts[arr[i]]] = arr[i]
    return temp

print(Counting(arr))