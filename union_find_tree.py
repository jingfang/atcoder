#%%
class UnionFind(object):
    def __init__(self,N):
        self.Parent = [-1] * N
    
    def root(self,i):
        if self.Parent[i] < 0:
            return i
        else:
            self.Parent[i] = self.root(self.Parent[i])
            return self.Parent[i]

    def size(self,i):
        return -self.Parent[i]


    #AとBの木をくっつける
    def connect(self,A,B):
        A = self.root(A)
        B = self.root(B)
        if A == B:
            return False
        #大きい方Aに小さい方Bをくっつけたいので、大小逆だったら交換
        if self.size(A)<self.size(B):
            A,B = B,A
        
        #くっつける=サイズの更新&Bの親をAにする
        self.Parent[A] += self.Parent[B]
        self.Parent[B] = A
            return True
#%%    
N,M = 4,5
bridge = [[1, 2], [3, 4], [1, 3], [2, 3],[1, 4]]
ans = [0]*M
ans[M-1] = N*(N-1)/2
#%%
Uni = UnionFind(N)

for i in range(M-1,0,-1):
    ans[i-1] = ans[i]
    a = bridge[i][0] - 1
    b = bridge[i][1] - 1
    print("iterate"+str(i))
    print(Uni.size(a),Uni.size(b))
    print(ans[i])
    if Uni.root(a) != Uni.root(b):
        ans[i-1] = ans[i] - Uni.size(a)*Uni.size(b)
        Uni.connect(a,b)
        print(ans[i-1])
        print(Uni.size(a),Uni.size(b))

#%%
for i in range(M):
    print(ans[i])
#%%
M=5
for i in range(M-1,0,-1):
    print(i)


#%%
bridge[M-1][1]

#%%
