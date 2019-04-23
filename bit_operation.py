#%%
# A=2
# B=4

A=123
B=456

ra = A%4
rb = B%4
#%%
#0b101^0b1100
# bin(0b101^0b100)
i = 1
j = 5
i^j
# i^j
# print(i)
# print(j)
print(i^j)
#%%
samp = 0
for i in range(40):
#    print(i,bin(i))
    samp = samp ^ i
    print(samp)


#%%
def f(x):
    rx = x%4
    bin_f = 0
    for i in range(rx+1): #add x, x-1, ..., x-rx (rx number in total)
        bin_f = bin_f ^ (x-i)
    return bin_f

#%%
[-1]*3

#%%
