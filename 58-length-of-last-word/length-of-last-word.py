class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #Length of current
        l = 0
        m = 0
        for letter in s:
            if letter == ' ':
                if l > 0:
                    m = l
                    l = 0
            else:
                l+=1
        
        if l > 0:
            m = l
        return m