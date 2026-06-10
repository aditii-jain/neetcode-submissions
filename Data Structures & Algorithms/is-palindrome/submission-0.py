class Solution:
    def isPalindrome(self, s: str) -> bool:
        # have a pointer from the front
        front = 0
        # have a pointer from the back
        back = len(s) - 1
        
        while front <= back:
            # process the character
            front_char = s[front]
            back_char = s[back]
            if not front_char.isalnum():
                front+=1
                continue
            if not back_char.isalnum():
                back-=1
                continue
            
                
            # keep checking str[front]==str[back]
            if front_char.lower() != back_char.lower():
                return False

            front+=1
            back-=1
        
        return True

        
        # as soon as it is not equal return false
        # at the end return true
        