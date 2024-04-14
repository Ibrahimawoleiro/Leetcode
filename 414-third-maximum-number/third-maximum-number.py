class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f = -(2**32)
        s = -(2**32)
        t = -(2**32)
        for val in nums:
            print(f,s,t)
            if val > f:
                temp = f
                f = val
                t = s
                s = temp
            elif val < f and val > s:
                s, t = t, s
                s = val
            elif val < s and val > t:
                t = val
        return t if t > -(2**32) else f



