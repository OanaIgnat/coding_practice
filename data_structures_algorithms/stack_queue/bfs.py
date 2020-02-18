# Queue
# code here
vis = [False] * N

queue = []
queue.append(0)
vis[0] = True

while queue:
    s = queue.pop(0)
    print(s, end=' ')
    for node in g[s]:
        if vis[node] == False:
            queue.append(node)
            vis[node] = True