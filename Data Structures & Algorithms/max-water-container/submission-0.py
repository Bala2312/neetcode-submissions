class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area= 0

        for i in range(n):
            for j in range(n):
                length = abs(j-i)
                breadth = min(heights[i],heights[j])
                area= length * breadth
                if area > max_area:
                    max_area=area
        return max_area


        