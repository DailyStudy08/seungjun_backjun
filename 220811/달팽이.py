# arr = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]
# r, c = 3, 3

# 상하좌우에 인접한 요소 차례대로 접근하기
# # 변화량 배열 선언
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# K = 3
# # i가 방향을 나타낸다
# for i in range(4):
#     # 바로 출력하는 것이 아니라.. K번 만큼 반복하면서 출력
#     for j in range(1, K + 1):
#         nr = r + dr[i] * j
#         nc = c + dc[i] * j
#         if N > nr >= 0 and N > nc >= 0:
#             print(arr[r + dr[i] * j][c + dc[i] * j])
#
# print('_______________________')
#
# # 시계방향
# di = [-1, -1, 0, 1, 1, 1, 0, -1]
# dj = [0, 1, 1, 1, 0, -1, -1, -1]
# for i in range(8):
#     print(arr[r + di[i]][c + dj[i]])

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

d = 0 # 달팽이가 움직일 방향을 정하는 변수
num = 1 # 달팽이가 지나간 위치에 적어줄 숫자
N = 5
arr =[[0] * N for _ in range(N)]
r, c = 0, 0 # 시작점

while num < N*N+1:
    # 달팽이 움직이기
    # 근데, 만약에 움직이려는 칸으로 못가면, 방향전환해주기
    print((r, c), num)
    arr[r][c] = num
    num += 1
    # 다음칸으로 이동, 내가 이동중인 방향으로 계속이동
    r += dr[d]
    c += dc[d]
    if r < 0 or r >= N or c < 0 or c >= N or arr[r][c] != 0: #범위 비정상
        r -= dr[d]
        c -= dc[d]
        # 방향전환
        d = (d + 1) % 4
        r += dr[d]
        c += dc[d]

print(arr)