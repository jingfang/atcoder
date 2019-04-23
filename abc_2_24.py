date = input()
year = date[:4]
month = date[5:7]
if int(year) < 2019:
        print("Heisei")
elif int(year)==2019:
    if month == "04":
        print("Heisei")
    elif month == "03":
        print("Heisei")
    elif month == "02":
        print("Heisei")
    elif month == "01":
        print("Heisei")
    else:
        print("TBD")
else:
        print("TBD")

type(month)
# date = input()
# year = date[:4]
# month = date[5:7]
# if int(year) < 2019:
#         print("Heisei")
# elif int(year)==2019 and month == "01" or "02" or "03" or "04":
#         print("Heisei")
# else:
#         print("TBD")


#%%
N = 5
A = 100
B = 90
C = 80
l = []
l.append(98)
l.append(40)
l.append(30)
l.append(21)
l.append(80)
uselist = [[],[],[],[]]
# l[0] = 98
# l[1] = 40
# l[2] = 30
# l[3] = 21
# l[4] = 80
# N, A, B, C =map(int,input().split())
# for i in range(N):
#     l[i] = input()
#%%
DFS(0,[],[],[],[])
#%%
uselist
#%%
uselist0 = []
u0 = uselist0 + [98]
u0
#%%
uselist = [[],[],[],[]]
uselist[0].append(98)
uselist[0].append(98)
print(uselist)
#%%
uselist
#%%
def DFS(i,uselist0,uselista,uselistb,uselistc):
    if i == N:
        uselist = [uselist0,uselista,uselistb,uselistc]
        return calc_mp(uselist)
    mplist = []
    u0 = uselist0 + [l[i]]
    ua = uselista + [l[i]]
    ub = uselistb + [l[i]]
    uc = uselistc + [l[i]]
    mplist.append(DFS(i+1, u0,uselista,uselistb,uselistc))
    mplist.append(DFS(i+1, uselist0,ua,uselistb,uselistc))
    mplist.append(DFS(i+1, uselist0,uselista,ub,uselistc))
    mplist.append(DFS(i+1, uselist0,uselista,uselistb,uc))
    return min(mplist)
#%%
uselist = [[None],[98],[40,30,21],[80]]
A = 100
B = 90
C = 80
calc_mp(uselist)
#%%
def calc_mp(uselist):
    mp = 0

    #合成魔法
    mp += (max(len(uselist[1]) - 1, 0)) * 10
    mp += (max(len(uselist[2]) - 1, 0)) * 10
    mp += (max(len(uselist[3]) - 1, 0)) * 10

    #その他魔法
    mp += abs(A - sum(uselist[1]))
    mp += abs(B - sum(uselist[2]))
    mp += abs(C - sum(uselist[3]))

    return mp



#%%

#%%
