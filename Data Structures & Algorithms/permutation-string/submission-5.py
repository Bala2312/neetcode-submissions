 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1="".join(sorted(s1))
        print(s1)
        s2_chars=[]
        window = len(s1)
        l = 0
        r = window -1
        while r < len(s2):
            check =[]
            for i in range(l,r+1):
                check.append(s2[i])
            if s1 == "".join(sorted(check)):
                return True
            l += 1
            r += 1
        return False

        
        
        









































