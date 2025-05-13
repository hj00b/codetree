n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def cnt_happy(arr):
    happy_row_cnt = 0
    for r in range(n):
        cnt = 1
        now_see = grid[r][0]
        for c in range(1, n):

            if now_see == grid[r][c]:
                cnt += 1

            else:
                now_see = grid[r][c]
                cnt = 1
                
            if cnt >= m:
                happy_row_cnt += 1
                break

    return happy_row_cnt


ans = 0
ans += cnt_happy(grid)

grid = list(zip(*grid))
ans += cnt_happy(grid)

print(ans)

