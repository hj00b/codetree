n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def cnt_happy(arr):
    happy_row_cnt = 0

    for row in arr:
        cnt = 1
        now_see = row[0]

        for x in row[1:]:
            if now_see == x:
                cnt += 1

            else:
                now_see = x
                cnt = 1

            if cnt >= m:
                happy_row_cnt += 1
                break
    return happy_row_cnt


if n == 1:
    print(2)
else:
    ans = cnt_happy(grid)
    new_grid = list(zip(*grid))
    ans += cnt_happy(new_grid)

    print(ans)