from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

# Please write your code here.
def bfs(sr, sc):
    visited = [[0]*n for i in range(n)]
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = 1

    total = 0
    ans = 0

    while queue:
        r, c = queue.popleft()
        vis = visited[r][c] 

        if grid[r][c]:
            # 금이 있다
            total += 1 
        k = vis - 1
        cost = k**2 + (k + 1)**2
        money = total * m - cost
        if money > 0:
            ans = max(ans, total)


        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
                visited[nr][nc] = vis + 1
                queue.append((nr, nc))

    return ans

total_ans = 0
for r in range(n):
    for c in range(n):
        res = bfs(r, c)
        total_ans = max(total_ans, res)


print(total_ans)
                
    
