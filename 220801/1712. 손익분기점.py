import sys
A, B, C = map(int, sys.stdin.readline().split())
cnt = 1
while True:
    if B-C >= 0:
        print(-1)
        break
    else:
        if B - C == -1:
            print(A + 1)
            break
        elif A+(B-C)*cnt < 0:
            print(cnt)
            break
        else:
            cnt += 1