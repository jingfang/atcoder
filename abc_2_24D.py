import bisect

A, B, Q = map(int, input().split())
INF = 10 ** 12
s = [-INF] + [int(input()) for i in range(A)] + [INF]
t = [-INF] + [int(input()) for i in range(B)] + [INF]
for q in range(Q):
    x = int(input())
    b,d = bisect.bisect_right(s,x) , bisect.bisect_right(t,x)
    res = INF
    for S in [s[b-1],s[b]]:
        for T in [t[d-1],t[d]]:
            d1 = abs(x-T) + abs(T-S) #t -> s
            d2 = abs(x-S) + abs(S-T) #s -> t
            res = min(res,d1,d2)
    print(res)