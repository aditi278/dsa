class Solution:
    def generateParenthesis(self, n: int, m=None, curr='', ans=None) -> List[str]:
        if m is None:
            m=n
        if ans is None:
            ans = []
        if n == 0 and m == 0:
            ans.append(curr)
            return ans
        if m > n:
            self.generateParenthesis(n, m-1, curr+')', ans)
        if n > 0:
            self.generateParenthesis(n-1, m, curr+'(', ans)
        return ans