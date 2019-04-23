import numpy as np

N,M = map(int,input().split())
data = []
for i in range(N):
    b = list(map(int,input().split())) # data = [[cost,max_num],...]
    data.append(b)
data.sort()

num_drink=0
cost=0
shop_index=0
while (shop_index < N and num_drink < M):
    num_drink += data[shop_index][1]
    cost += data[shop_index][0]*data[shop_index][1]
    shop_index += 1
excess = num_drink - M
ans = cost - data[shop_index-1][0] * excess
print(ans)
