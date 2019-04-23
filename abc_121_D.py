import numpy as np

A,B = map(int,input().split())
def f(x):
    rx = x%4
    bin_f = 0
    for i in range(rx+1): #add x, x-1, ..., x-rx (rx number in total)
        bin_f = bin_f ^ (x-i)
    return bin_f

print(f(A-1)^f(B))