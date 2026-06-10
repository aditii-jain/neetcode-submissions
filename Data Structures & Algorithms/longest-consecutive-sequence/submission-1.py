class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        max = 0
        nums.sort()
        print(nums)
        curr = 0
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                curr+=1
            elif nums[i]!=nums[i+1]:
                curr = 0
            if curr > max:
                max = curr
        return max + 1