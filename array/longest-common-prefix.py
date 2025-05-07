class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=strs[0]
        for x in strs:
            i = 0 
            while i< min(len(pre), len(x)):
                if pre[i] != x[i]:
                    break
                i+=1
            pre = pre[:i]
        return pre
