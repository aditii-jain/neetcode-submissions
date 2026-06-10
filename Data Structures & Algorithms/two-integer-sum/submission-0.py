class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [3,4,5,6], target = 7
        # Output: [0,1]
        val_index = {}
        for i, num in enumerate(nums):
            if target - num in val_index:
                return [val_index[target-num],i]
            val_index[num] = i
        
        