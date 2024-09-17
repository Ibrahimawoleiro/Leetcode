class Solution:
    def brute_force(self,s):
        i = 0
        ans = 0
        while i < len(s):
            index = i
            store = set()
            size = 0
            while index < len(s):
                if s[index] not in store:
                    print(s[index])
                    size += 1
                    store.add(s[index])
                else:
                    break
                index += 1
            print(ans, size)
            ans = max(ans, size)
            i += 1
        return ans
    
    def optimized(self,s):
        l = 0
        r = 0
        ans = 0
        store = {}
        while r < len(s):
            if s[r] not in store or store[s[r]] < l:
                ans = max(ans, r - l + 1)
                store[s[r]] = r
                r += 1
            else:
                l = store[s[r]] + 1
        return ans
            
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.optimized(s)