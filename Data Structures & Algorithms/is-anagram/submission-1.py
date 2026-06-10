class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_char_s = [0]*26
        count_char_t = [0]*26
        for c in s:
            count_char_s[ord(c)-ord('a')]+=1
        for c in t:
            count_char_t[ord(c)-ord('a')]+=1
        return count_char_s == count_char_t
        