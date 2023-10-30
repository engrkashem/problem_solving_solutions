'''
class Solution:
    def findRedundantConnection(self, edges):
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        # print(parent)
        # print(rank)

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        # return False if already unioned
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            print(p1, p2)
            print(parent)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            print(n1, n2, ' n1,n2')
            if not union(n1, n2):
                return [n1, n2]
'''


class Disjoint:
    def __init__(self, n):
        self.rank = [0]*(n+1)
        self.parent = [i for i in range(n+1)]

    def findUpar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUpar(self.parent[node])
        return self.parent[node]

    def byRank(self, u, v):
        ulp_u = self.findUpar(u)
        ulp_v = self.findUpar(v)
        if ulp_u == ulp_v:
            return False
        if self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_u] = ulp_v
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        disjoint = Disjoint(n)
        for x, y in edges:
            if disjoint.byRank(x, y) == False:
                lst = [x, y]
        return lst


obj = Solution()

edges = [[1, 2], [1, 3], [2, 3]]

# edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]

print(obj.findRedundantConnection(edges))
