class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque

        stack = deque()
        i= 0
        ans =0
        while i < len(tokens):
            if tokens[i] not in "+-/*":
                stack.append(int(tokens[i]))
            else:
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == "+":
                    stack.append(a+b)
                elif tokens[i] == "*":
                    stack.append(a*b)
                elif tokens[i] == "-":
                    stack.append(b-a)
                elif tokens[i] == "/":
                    stack.append(int(b/a))
            i +=1 
        return stack[-1]
            
        

        