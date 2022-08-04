def push(x):
    return queue.append(x)

def pop(queue):
    if queue == []:
        return -1
    else:
        return queue.pop(0)

def size(queue):
    return len(queue)

def empty(queue):
    if queue == []:
        return 1
    else:
        return 0

def front(queue):
    if queue == []:
        return -1
    else:
        return queue[0]

def back(queue):
    if queue == []:
        return -1
    else:
        return queue[-1]

queue = []

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    order = list(map(str, input().rstrip().split()))
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'pop':
        print(pop(queue))
    elif order[0] == 'size':
        print(size(queue))
    elif order[0] == 'empty':
        print(empty(queue))
    elif order[0] == 'front':
        print(front(queue))
    elif order[0] == 'back':
        print(back(queue))



