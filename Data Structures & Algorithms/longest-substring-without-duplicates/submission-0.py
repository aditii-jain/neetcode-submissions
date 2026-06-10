class Solution:
    def hasDuplicates(self, l:int, r:int, s:str) -> bool:
        while l < r:
            if s[l] == s[r]: return True
            l+=1
        return False

    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # have 2 pointers l, r
        # both start at position 0

        l, r = 0, 0
        max_length = 0

        while l <= r and r < len(s):
            substring = s[l:r+1]
            print(substring)
            length = len(substring)

            

            if length == 1 or not self.hasDuplicates(l,r, s):
                if length > max_length:
                    max_length = length
                r+=1
            else: 
                l+=1

            print(max_length)


        

        return max_length

    


        