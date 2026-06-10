class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        og_len = len(nums)
        nums = set(nums)
        now_len = len(nums)
        return not og_len == now_len