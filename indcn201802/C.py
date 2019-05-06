T, S = map(int, input().split())
a = list(map(int, input().split()))

def solve():
	prefix = [0]
	for t in a:
		prefix.append(t + prefix[-1])
	prefix.pop(0)

	max_prefix = max(prefix)
	if max_prefix < S and prefix[-1] <= 0:
		return -1
	
	temp = max(S - max_prefix, 0)
	cnt = temp // prefix[-1] * T
	temp = temp // prefix[-1] * prefix[-1]



	for t in a + a:
		if temp >= S:
			return cnt
		cnt += 1
		temp += t

print(solve())
