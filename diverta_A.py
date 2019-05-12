import math
N = int(input())
ans = 0
for p in range(1, math.floor(-1/2+math.sqrt((1+4*N))/2)+1):
    # print(p)
    if N % p == 0:
        m = N//p -1
        ans += m
        # print(m)
print(ans)
# bridge = [list(map(int, input().split())) for i in range(N)]
# print(N,M,bridge)