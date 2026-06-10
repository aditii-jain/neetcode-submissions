class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        
        max_volume = 0

        while l < r and r < len(heights):
            volume = min(heights[l], heights[r]) * (r-l)
            if volume > max_volume:
                max_volume = volume
            
            l+=1

            if l == r:
                r -= 1
                l = 0
        return max_volume
            

        