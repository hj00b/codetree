n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0

for i in range(0, n - 2):
    for j in range(0, n - 2):
        total = 0
        for k in range(3):
            for m in range(3):
                total += grid[i+k][j+m]
        ans = max(ans, total)


print(ans)