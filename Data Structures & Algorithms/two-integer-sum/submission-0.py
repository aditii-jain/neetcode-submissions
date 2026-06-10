class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, num in enumerate(nums):
            second_num = target - num # 7-4=3
            if second_num in visited:
                return [visited[second_num], i]
            visited[num] = i
        
        return []