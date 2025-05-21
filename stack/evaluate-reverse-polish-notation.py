class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for x in tokens:
            if x == "+":
                s.append(s.pop() + s.pop())
            elif x == "*":
                s.append(s.pop() * s.pop())
            elif x == "/":
                num2 = s.pop()
                num1 = s.pop()
                s.append(int(num1 / num2))
            elif x == "-":
                num2 = s.pop()
                num1 = s.pop()
                s.append(num1 - num2)
            else:
                s.append(int(x))
        return s[0]    