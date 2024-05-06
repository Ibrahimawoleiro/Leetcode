class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_length = 0
        c = set()
        l = 0
        r = 0

        while(r < len(s)):
            if s[r] not in c:
                c.add(s[r])
                if r - l + 1 > max_length:
                    max_length = (r - l ) + 1
                r+=1
            else:
                c.remove(s[l])
                l += 1
        
        return max_length