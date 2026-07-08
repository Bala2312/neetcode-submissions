from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return True
        if len(s) % 2 != 0:
            return False

        stack = deque()
        stack.append(s[0])

        i = 1

        while i < len(s):
            if s[i] == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
            elif s[i] == "}":
                if not stack or stack[-1] != "{":
                    return False

                stack.pop()

            elif s[i] == ")":
                if not stack or stack[-1] != "(":
                    return False

                stack.pop()

            elif s[i] in "[{(":
                stack.append(s[i])

            i += 1

        return not stack