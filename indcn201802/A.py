N = int(input())


# def get_dp(N):
#     dp = [0 for i in range(N + 1)]
#     dp[1] = 0
#     for i in range(2, N + 1):
#         if i % 2 != 0:
#             dp[i] = dp[i - 1] + 1
#         else:
#             dp[i] = min(dp[i - 1], dp[i // 2]) + 1
#     return dp[-1]


def solve(N):
    step = 0
    q = [N]
    m = set()
    while q:
        new_q    = []
        for t in q:
            if t == 1:
                return step
            if t % 2 == 0:
                if (t // 2) not in m:
                    m.add(t // 2)
                    new_q.append(t // 2)
            if t - 1 not in m:
                m.add(t - 1)
                new_q.append(t - 1)
        q = new_q
        step += 1

# def solve(N):
#     step = 0
#     q = [1]
#     m = set()

#     while q:
#         new_q = []
#         for t in q:
#             if t == N:
#                 return step
#             for p in [t * 2, t + 1]:
#                 if p <= 10**18 and p not in m:
#                     m.add(p)
#                     new_q.append(p)
#         q = new_q
#         step += 1

print(solve(N))
