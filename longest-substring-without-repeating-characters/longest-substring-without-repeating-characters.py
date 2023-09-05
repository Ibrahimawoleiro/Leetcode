class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        create a variable left = 0
        create a variable right = 0
        create a variable count = 0
        create a variable maximum = 0
        
        create a set called dict
        
        create a while loop that runs as long as right is less than the length of s
            if letter is not in dict
                add it to the dictionary and increase count by 1
                check if the value in count is greater than maximum
                    if yes, update maximum to count
                increment the value of right by one
            if the letter is in dict:
                if the letter at left != letter at right and left < right:
                    keep increasing left by one 
                    decrement count by one
                else if the letter at left == letter at right and left < right:
                    increment left by one
                    decrement count by one
                else if the letter at left == letter at right and left == right:
                    increment right by one
                    increment count by one
                    
        """
        left = 0
        right = 0
        count = 0
        maximum = 0
        
        dictionary = set()
        
        while right < len(s):
            if s[right] not in dictionary:
                dictionary.add(s[right])
                count+=1
                maximum = max(maximum,count)
                right+=1
            else:
                if s[left] != s[right] and left < right:
                    dictionary.remove(s[left])
                    left+=1
                    count-=1
                elif s[left] == s[right] and left < right:
                    left+=1
                    right+=1
                elif s[left] == s[right]  and left == right:
                    right+=1
                
        
        return maximum
            
            
            