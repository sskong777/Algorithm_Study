n = int(input())  
m = int(input())  

graph = [[] for _ in range(n + 1)] 
visited = [False] * (n + 1) 

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [1] 
visited[1] = True 

count = 0 

while stack:
    v = stack.pop()
    count += 1

    for i in graph[v]:
        if not visited[i]:
            stack.append(i)
            visited[i] = True

count -= 1 

print(count)
