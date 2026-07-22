 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars =[]
        s2_chars=[]
        for char in s1:
            s1_chars.append(char)
        s1_sorted = "".join(sorted(s1_chars))
        window = len(s1_chars)
        l = 0
        r = window -1
        while r < len(s2):
            check =[]
            for i in range(l,r+1):
                check.append(s2[i])
            if s1_sorted == "".join(sorted(check)):
                return True
            l += 1
            r += 1
        return False

        
        
        









































