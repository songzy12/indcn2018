N, Q = map(int, input().split())
A = list(map(int, input().split()))
sum_even = sum([x for x in A if x % 2 == 0])
sum_odd = sum([x for x in A if x % 2 == 1])

def is_even(x):
    return x % 2 == 0

for i in range(Q):
    index, delta = map(int, input().split())
    index -= 1
    if is_even(A[index]) and is_even(delta):
        sum_even += delta
        A[index] += delta
    elif is_even(A[index]) and not is_even(delta):
        sum_even -= A[index]
        A[index] += delta
    elif not is_even(A[index]) and is_even(delta):
        A[index] += delta
    elif not is_even(A[index]) and not is_even(delta):
        sum_even += A[index] + delta
        A[index] += delta
    print(sum_even)