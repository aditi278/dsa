class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for x in s:
            if x == '(' or x == '{' or x == '[':
                l.append(x)
            elif len(l) == 0:
                return False
            else:
                par = l.pop()
                if (x == ')' and par != '(') or (x == '}' and par != '{') or (x == ']' and par != '['):
                    return False
        if len(l) == 0:
            return True
        else:
            return False
