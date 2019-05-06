H, W = map(int, input().split())
grid = []
for i in range(H):
    grid.append(input())

dp_left = {}
dp_right = {}

mod = 10**9+7


def get_dp_left(i, j):
    if grid[0][0] != '.':
        return 0
    if (i, j) in dp_left:
        return dp_left[i, j]
    if grid[i][j] == '#':
        return 0
    if i == 0 and j == 0:
        return 1
    temp = 0
    if i - 1 >= 0 and grid[i-1][j] == '.':
        temp += get_dp_left(i-1, j)
    if j - 1 >= 0 and grid[i][j-1] == '.':
        temp += get_dp_left(i, j-1)
    dp_left[i, j] = temp % mod
    return dp_left[i, j]


def get_dp_right(i, j):

    if grid[-1][-1] == '#':
        return 0
    if (i, j) in dp_right:
        return dp_right[i, j]
    if grid[i][j] == '#':
        return 0
    if i == H - 1 and j == W - 1:
        return 1
    temp = 0
    if i + 1 < H and grid[i+1][j] == '.':
        temp += get_dp_right(i+1, j)
    if j + 1 < W and grid[i][j+1] == '.':
        temp += get_dp_right(i, j+1)
    dp_right[i, j] = temp % mod
    return dp_right[i, j]


Q = int(input())
for q in range(Q):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    print((get_dp_left(i, j) * get_dp_right(i, j)) % mod)
