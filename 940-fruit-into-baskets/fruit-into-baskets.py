class Solution:
    def optimized(self,fruits):
        allowed = 2
        l = 0
        r = 0
        n = len(fruits)
        ans = 0
        checker = {}
        while r < n:
            if fruits[r] in checker:
                checker[fruits[r]] += 1
            else:
                checker[fruits[r]] = 1
            while len(checker) > allowed:
                checker[fruits[l]] -= 1
                if checker[fruits[l]] == 0:
                    del checker[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans
    def totalFruit(self, fruits: List[int]) -> int:
        return self.optimized(fruits)