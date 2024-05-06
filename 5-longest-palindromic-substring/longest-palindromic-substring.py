class Solution:
    def longestPalindrome(self, s: str) -> str:
        #max sub
        m = ''
        #loop through the word
        for index in range(len(s)):
            
            #Odd case

            i = index
            j = index
            #While the subarr is still a palindrom
            #And i and j are valid indices
            while(i>=0 and j<len(s) and s[i] == s[j]):
                if (j - i)+ 1 > len(m):
                    m = s[i: j+1]
                i-=1
                j+=1

            #Even case
            i = index
            j = index + 1
            while(i >= 0 and j < len(s) and s[i] == s[j]):
                if (j - i)+ 1 > len(m):
                    m = s[i: j+1]
                i-=1
                j+=1
        return m