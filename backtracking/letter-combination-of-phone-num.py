class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        n = len(digits)
        digitsToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def recurse(i=0, currStr=""):
            if len(currStr) == n:
                res.append(currStr)
                return
            for x in digitsToChar[digits[i]]:
                recurse(i+1, currStr+x)
        
        if n:
            recurse()
        return res