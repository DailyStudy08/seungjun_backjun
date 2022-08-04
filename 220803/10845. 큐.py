def push(x):
    return que.append(x)

def pop(que):
    if que == []:
        return -1
    else:
        return que.pop(0)

def size(que):
    return len(que)

def empty(que):
    if que == []:
        return 1
    else:
        return 0

def front(que):
    if que == []:
        return -1
    else:
        return que[0]

def back(que):
    if que == []:
        return -1
    else:
        return que[-1]

que = []

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    order = list(map(str, input().rstrip().split()))
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'pop':
        print(pop(que))
    elif order[0] == 'size':
        print(size(que))
    elif order[0] == 'empty':
        print(empty(que))
    elif order[0] == 'front':
        print(front(que))
    elif order[0] == 'back':
        print(back(que))



