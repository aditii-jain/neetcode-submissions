from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # loop through the array 
            # count each occurrence in dictionary
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        res = []
        # [1,1,2,2,5]
        # 1: 2, 2: 2, 5: 1

        buckets = [[] for _ in range(len(nums)+1)]
        for n, c in count.items():
            buckets[c].append(n)
        
        
        for bucket in range(len(buckets)-1, -1, -1):
            for val in buckets[bucket]:
                res.append(val)

                if len(res) == k:
                    return res

        return res


