# 타임머신

INF = int(1e9)
n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))
    
def bf():
    dist = [INF]*(n+1)
    dist[1] = 0
    for i in range(n):
        for [s,e,w] in graph:
            if dist[s] != INF and dist[s]+w < dist[e]:
                dist[e] = dist[s]+w
                if i == n-1:
                    print(-1)
                    return
    for j in range(2,n+1):
        print(-1 if dist[j] == INF else dist[j])
      
bf()