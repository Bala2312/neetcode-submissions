class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_new = "".join(sorted(s))
        t_new = "".join(sorted(t))

        return s_new == t_new
        

            
        