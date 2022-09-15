import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, root):
    global tree, visited
    tree[n] = -9999
    visited[n] = 1
    for i in range(root, len(tree)):
        if not visited[i]:
            dfs(n, i+1)

# 노드의 갯수
V = int(input())
E = V - 1
tree = list(map(int, input().split()))
# 지울 노드
x = int(input())
visited = [0]*(V)

dfs(x, 0)




