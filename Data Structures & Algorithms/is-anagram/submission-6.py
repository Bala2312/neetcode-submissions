class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = [0]*26
        arr2 = [0]*26

        for char in s:
            arr1[ord(char) - ord('a')]+=1
        for char in t:
            arr2[ord(char) - ord('a')]+=1
        return arr1 == arr2


            
        