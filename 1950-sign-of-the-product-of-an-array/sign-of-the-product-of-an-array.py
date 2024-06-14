class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count_0 = 0
        count_n = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                count_n += 1

        if count_n % 2 == 1:
            return -1

        return 1