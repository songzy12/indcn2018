N, Q = map(int, input().split())
a = list(map(int, input().split()))



from itertools import product

class RangeMinimum(object):
    "Data structure providing efficient range-minimum queries."

    def __init__(self, numbers):
        "Build a RangeMinimum object for the given sequence of numbers."
        # Mapping from (start, step) to min(numbers[start:start + 2**step])
        self._rmq = rmq = {(i, 0): m for i, m in enumerate(numbers)}
        n = len(numbers)
        for step, i in product(range(1, n.bit_length()), range(n)):
            j = i + 2 ** (step-1)
            if j < n:
                rmq[i, step] = min(rmq[i, step-1], rmq[j, step-1])
            else:
                rmq[i, step] = rmq[i, step-1]

    def query(self, start, stop):
        "Return min(numbers[start:stop])."
        j = (stop - start).bit_length() - 1
        x = self._rmq[start, j]
        y = self._rmq[stop - 2 ** j, j]
        return min(x, y)

prefix = [0]
for t in a:
	prefix.append(t+prefix[-1])


a = RangeMinimum(prefix)
b = RangeMinimum([-x for x in prefix])

def solve(l, r):
	return abs(-b.query(l, r+2) - a.query(l, r+2))

# prefix[i] is sum(a[:i])

# print (prefix)
# def solve(l, r):
# 	# print(prefix[l:r+2])
# 	return abs(max(prefix[l:r+2]) - min(prefix[l:r+2]))




for q in range(Q):
    l, r = map(int, input().split())
    print(solve(l - 1, r - 1))
