import numpy as np
import sys

# N,M = map(int,input().split())
# bridge = [list(map(int, input().split())) for i in range(N)]
# print(N,M,bridge)

N,M = 4,5
bridge = [[1, 2], [3, 4], [1, 3], [2, 3]]

unconnected_pairs = N*(N-1)/2

for i in range(M):

    if unconnected_pairs == 0:
        break