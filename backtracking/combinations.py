class Solution:
    def combine(self, n: int, k: int, combi=None, curr=None) -> List[List[int]]:
        if combi is None:
            combi = []
        if curr is None:
            curr = []
        if n < k:
            return combi
        if k == 0:
            n_curr = []
            for x in curr:
                n_curr.append(x)
            combi.append(n_curr)  
            return combi
        for i in range(n, 0, -1):
            curr.append(i)
            self.combine(i-1, k-1, combi, curr)
            curr.pop()
        curr = []
        return combi   