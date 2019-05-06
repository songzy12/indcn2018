N = int(input())
X = list(map(int, input().split()))


def solve():
    l = 0
    r = N - 1
    while l < len(X) - 1 and abs(X[l]) >= abs(X[l + 1]):
        l += 1
    while r > 0 and abs(X[r - 1]) <= abs(X[r]):
        r -= 1

    if l < r:
        return -1
    cnt = 0
    # print(r)
    for x in X[:r]:
        if x > 0:
            cnt += 1
    # print(l)
    for x in X[l+1:]:
        if x < 0:
            cnt += 1

    while r < l and X[r] <= 0:
        r += 1
    while r < l and X[l] >= 0:
        l -= 1
    cnt1 = 0
    cnt0 = 0

    for x in X[r:l+1]:
        if x < 0:
            cnt1 += 1
        else:
            cnt0 += 1
    # print(cnt, cnt1, cnt0)
    return cnt + min(cnt0, cnt1)


print(solve())
