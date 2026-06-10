class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        circular_rob2 = 0
        for i in range(1, len(nums)):
            temp = max(rob1 + nums[i], rob2)
            rob1 = rob2 
            rob2 = temp
        
        temp = 0
        rob1 = 0
        for i in range(len(nums)-1):
            temp = max(rob1 + nums[i], circular_rob2)
            rob1 = circular_rob2 
            circular_rob2 = temp
        
        return max(nums[0], rob2, circular_rob2)