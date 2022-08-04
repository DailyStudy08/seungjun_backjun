import sys
input = sys.stdin.readline

n = int(input())
word_list = []

for _ in range(n):
	word_list.append(input().strip())
word_list = list(set(word_list))  # 중복 제거
word_list.sort(key = lambda x: (len(x), x)) # 정렬
print(word_list)