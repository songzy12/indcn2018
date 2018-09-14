H, W = map(int, input().split())
grid = []
for i in range(H):
    grid.append(input())

mod = 10**9+7

left = [[0 for i in range(W)] for j in range(H)]
right = [[0 for i in range(W)] for j in range(H)]

if grid[0][0] == '.':
    left[0][0] = 1
    for i in range(1, W):
        if grid[0][i] == '.':
            left[0][i] = (left[0][i - 1]) % mod
        else:
            break
    for j in range(1, H):
        if grid[j][0] == '.':
            left[j][0] = (left[j - 1][0]) % mod
        else:
            break
    for i in range(1, H):
        for j in range(1, W):
            if grid[i][j] != '.':
                continue
            left[i][j] = (left[i-1][j] + left[i][j-1]) % mod
# for row in left:
#     print(row)
# print()
if grid[-1][-1] == '.':
    right[-1][-1] = 1
    for i in range(W - 2, -1, -1):
        if grid[-1][i] == '.':
            right[-1][i] = (right[-1][i+1]) % mod
        else:
            break
    for j in range(H - 2, -1, -1):
        if grid[j][-1] == '.':
            right[j][-1] = (right[j+1][-1]) % mod
        else:
            break
    for i in range(H - 2, -1, -1):
        for j in range(W - 2, -1, -1):
            if grid[i][j] != '.':
                continue
            right[i][j] = (right[i+1][j] + right[i][j+1]) % mod
# for row in right:
#     print(row)
# print()
Q = int(input())
for q in range(Q):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    print((left[i][j] * right[i][j]) % mod)
