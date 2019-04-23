
#%%
import numpy as np
N, M =map(int,input().split())
search = np.zeros(M+1)
for i in range(N):
    K = list(map(int,input().split()))
    for j in range(1,K[0]+1):
        search[K[j]]+=1
place = np.where(search==N)
print(len(place[0]))

#%% [markdown]
# #### import numpy as np
# N, M =map(int,input().split())
# search = np.zeros(M)
# print(search)

#%%
import numpy as np
N, M =map(int,input().split())
search = np.zeros(M+1)
for i in range(N):
    K = list(map(int,input().split()))
    for j in range(1,K[0]+1):
        search[K[j]]+=1
place = np.where(search==N)
print(search)
print(place)
print(len(place))


#%%
search = np.zeros(6)
search += 4
search[0]-=4
print(search)
place = np.where(search==N)
print(len(place[0]))


#%%
N, M = map(int,input().split())
listA = list(map(int,input().split()))
needM = [2,5,5,4,5,6,3,7,6]
listM = [needM[i-1] for i in listA]
print(listM)


#%%
listA = list(map(int,input().split()))
needM = [2,5,5,4,5,6,3,7,6]
listM = [needM[i-1] for i in listA]
print(listM)


#%%
import math
N,M = 20,4
# N, M = map(int,input().split())
# listA = list(map(int,input().split()))
# needM = [2,5,5,4,5,6,3,7,6]
# listM = [needM[i-1] for i in listA]
unique_list = sorted(list(set(listM)))
print(unique_list)


#%%
import math
N,M = 20,4
unique_list = sorted(list(set(listM)))
print(unique_list)
# ax+by+cz+...=A coeff=[a,b,c,...] ans=A
# if true ax+by+cz+...=A has integer answers
def HasAnswer(coefficients,ans):
    if len(coefficients) == 1:
        return coefficients[0] % ans == 0
    else:
        residue = ans % gcd_all(coefficients)
        return residue == 0


#%%
import math
numberlist = [3,6]
def gcd_all(numberlist):
    currentgcd = numberlist[0]
    for i in numberlist[1:]:
        #print(i)
        currentgcd = math.gcd(currentgcd,i)
    return currentgcd


#%%
for i in range(len(unique_list)):
    HasAnswer(unique_list[:i+1])


#%%
gcd_all([3,6,5])


#%%
HasAnswer([3,5],4)


