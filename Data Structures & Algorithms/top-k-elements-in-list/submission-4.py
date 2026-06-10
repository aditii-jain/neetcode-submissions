from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         Input: nums = [1,2,2,3,3,3], k = 2
#         Output: [2,3]
        val_count = defaultdict(int)
        for num in nums:
            val_count[num] += 1
        
        # val_count = {1:1,2:2,3:3}
        count_values = [[] for i in range(len(nums)+1)]
        for key,val in val_count.items():
            count_values[val].append(key)
        
        print(count_values)
        res = []
        for i in range(len(nums),0,-1):
            if len(count_values[i]):
                for val in count_values[i]:
                    res.append(val)
                if len(res) >= k:
                    return res
        return res 
            
