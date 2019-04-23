#%%
import numpy as np
hello = np.arange(12)[::-1].reshape(2,2,3)
h0 = np.sort(hello, axis=0)
h1 = np.sort(hello, axis=1)
h2 = np.sort(hello, axis=2)


#%%
print(hello)
print(h0)
print(h1)
print(h2)

#%%
hellolist = [[[11,10,9],[8,7,6]],[[5,4,3],[2,1,0]]]
print(hellolist)
print(sorted(hellolist))
#%%
hellolist = [[4,5,3],[2,1,0]]
print(hellolist)
print(sorted(hellolist,key=lambda x: x[2]))
#sortedはデフォルトで一個めの引数でソートするみたい
hellolist.sort()
print(hellolist)
#%%
