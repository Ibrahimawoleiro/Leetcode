class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        store = {'a':-1,
                 'b':-1,
                 'c':-1
                 }
        ans = 0
        for index in range(len(s)):
            store[s[index]] = index
            if store['a'] >= 0 and store['b'] >= 0 and store['c'] >= 0:
                min_start = min(store['a'], store['b'], store['c'])
                ans += min_start + 1

        return ans