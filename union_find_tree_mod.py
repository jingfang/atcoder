class UnionFind(object,N):
    def __init__(self):
        self.Parent = [-1]*N
    
    def root(self,i):
        if self.Parent[i] < 0:
            return i
        else:
            return self.Parent[i] = root(self.Parent[i])
    def size(i):
        return -self.Parent[i]

    #AとBの木をくっつける
    def connect(A,B):
        A = root(A)
        B = root(B)
        if A == B:
            return False
        #大きい方Aに小さい方Bをくっつけたいので、大小逆だったら交換
        if size(A)<size(B):
            A,B = B,A
        
        #くっつける=サイズの更新&Bの親をAにする
        self.Parent[A] += self.Parent[B]
        self.Parent[B] = A
        
N,M = 4,5
bridge = [[1, 2], [3, 4], [1, 3], [2, 3],[1,4]]
ans = [0]*M
ans[M-1] = N*(N-1)/2

Uni = UnionFind(N)