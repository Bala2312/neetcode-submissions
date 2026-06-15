class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        
        # Count frequency
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        # Sort by frequency (descending)
        sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
        
        # Take top k elements
        return [item[0] for item in sorted_items[:k]]