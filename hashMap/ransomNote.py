class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l = {}
        for x in magazine:
            if x in l.keys():
                l[x]+=1
            else:
                l[x]=1
        for x in ransomNote:
            if x not in l.keys():
                return False
            if l[x] <= 0:
                return False
            l[x] -= 1
        return True