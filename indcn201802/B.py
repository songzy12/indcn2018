N, M = map(int, input().split())

from collections import defaultdict
parent = defaultdict(list)
degree = defaultdict(int)
for m in range(M):
    p, q = map(int, input().split())
    parent[q].append(p)
    degree[p] += 1

dp = {1: 1}


def get_dp(k):
	if k in dp:
		return dp[k]
	res = 0
	for t in parent[k]:
		res += get_dp(t) * 1.0 / degree[t]
	dp[k] = res
	return dp[k]

if degree[N] > 0:
    print(0)
else:
    print(get_dp(N))
