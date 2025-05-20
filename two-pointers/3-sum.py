class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        p = []
        n = []
        z = []
        for x in nums:
            if x<0:
                n.append(x)
            elif x>0:
                p.append(x)
            else:
                z.append(x)
        N = set(n)
        P = set(p)
        if len(z)>= 3:
            res.add(tuple([0,0,0]))
        if len(z) > 0:
            for x in P:
                if -x in N:
                    res.add(tuple([-x, 0, x]))
        
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                if -(p[i]+p[j]) in N:
                    res.add(tuple(sorted([p[i], p[j], -(p[i]+p[j])])))
        
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                if -(n[i]+n[j]) in P:
                    res.add(tuple(sorted([n[i], n[j], -(n[i]+n[j])])))
        
        arr = []
        for x in res:
            arr.append(list(x))
        return arr

        