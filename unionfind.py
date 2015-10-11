class QuickFind(object):
    def __init__(self,N=0):
        self.N = N
        self.id = range(self.N)

    def find(self,p,q):
        return self.id[p] == self.id[q]

    def unite(self,p,q):
        pid = self.id[p]
        for i in range(self.N): 
            if self.id[i] == pid: self.id[i] = self.id[q]

qf = QuickFind(10)
qf.unite(1,9)
# print qf.find(1,9)


class QuickUnion(object):
    def __init__(self,N=0):
        self.N = N
        self.id = range(self.N)

    def root(self,i):
        while i != self.id[i]: i = self.id[i]
        return i

    def find(self,p,q):
        return self.root(p) == self.root(q)

    def unite(self,p,q):
        self.id[self.root(p)] = self.root(q)


qu = QuickUnion(10)
qu.unite(3,4)
qu.unite(4,9)
qu.unite(8,0)
qu.unite(2,3)
qu.unite(5,6)
qu.unite(5,9)
# print qu.find(6,9)

class WeightedQuickUnion(object):
    def __init__(self,N=0):
        self.N = N
        self.id = range(self.N)
        self.sz = [0]*self.N

    def root(self,i):
        while i != self.id[i]: i = self.id[i]
        return i

        
    def find(self,p,q):
        return self.root(p) == self.root(q)

    def unite(self,p,q):
        # merge smaller trees into larger tree
        if self.sz[p] < self.sz[q] : 
            self.id[p] = q
            self.sz[q] += self.sz[p]

        else:
            self.id[q] = p
            self.sz[p] += self.sz[q]

wqu = WeightedQuickUnion(10)
wqu.unite(3,4)
wqu.unite(4,9)
wqu.unite(8,0)
wqu.unite(2,3)
wqu.unite(5,6)
wqu.unite(5,9)

print wqu.find(8,3)



