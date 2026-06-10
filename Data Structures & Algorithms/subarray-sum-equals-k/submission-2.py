

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0]=1
        sum = 0
        res = 0
        for num in nums:
            sum += num
            target = sum - k
            if target in prefixSum:
                res += prefixSum[target]
            prefixSum[sum]+=1
        
        return res

