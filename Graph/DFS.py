def DFS(start):
    stack=[start]
    while stack:
        parent=stack.pop()
        if(not visited[parent]):
            visited[parent]=True
            print(parent,end=' ')
            for child in graph[parent]:
                if (not visited[child]):
                    stack.append(child)
    print()
    return
n,m,start=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[False]*(n+1)
DFS(start)


# example for input:
# 10 10 0
# 0 1
# 0 3
# 0 2
# 1 4
# 3 5
# 5 7
# 3 6
# 2 8
# 8 9
# 9 10


