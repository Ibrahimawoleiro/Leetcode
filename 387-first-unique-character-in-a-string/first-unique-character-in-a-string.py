class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        ans = -1

        store = {}

        for l in s:
            if l in store:
                store[l] += 1
            else:
                store[l] = 1

        for i in range(len(s)):
            if store[s[i]] == 1:
                ans = i
                break
        
        return ans
