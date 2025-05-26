class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str, memo=None) -> bool:
        if memo is None:
            memo={}
        if len(s3) != len(s1) + len(s2):
            return False
        if len(s3) == len(s2) == len(s1) == 0:
            return True
        if tuple([s1, s2, s3]) in memo:
            return memo[tuple([s1, s2, s3])]
        if tuple([s2, s1, s3]) in memo:
            return memo[tuple([s2, s1, s3])]
        if len(s1) and s1[0] == s3[0]:
            if self.isInterleave(s1[1:], s2, s3[1:], memo):
                memo[tuple([s1, s2, s3])] = True
                return True
        if len(s2) and s2[0] == s3[0]:
            if self.isInterleave(s1, s2[1:], s3[1:], memo):
                memo[tuple([s1, s2, s3])] = True
                return True
        memo[tuple([s1, s2, s3])] = False
        return False