n, m = map(int, input().split())

visited = [0]*(n+1)
answer = []

def dfs(a):
    if a == 0:
        print(' '.join(map(str, answer)))
        return

    for i in range(1, n+1):
        if not visited[i]:
            answer.append(i)
            visited[i] = 1
            dfs(a-1)
            visited[i] = 0
            answer.pop()

dfs(m)