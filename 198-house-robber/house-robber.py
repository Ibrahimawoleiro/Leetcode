class Solution:
    def rob(self, nums: List[int]) -> int:
        dic = {}
        def helper(i):
            if i >= len(nums):
                return 0

            if i in dic:
                return dic[i]
            m = 0
            for r in range(i+2, len(nums)):
                #right neighbor
                n = helper(r)
                if n > m:
                    m = n
            dic[i] = m + nums[i]

            return dic[i]
        helper(0)
        helper(1)
        print(dic)
        if len(nums) > 1:
            if 1 in dic:
                return max(dic[0], dic[1])
        return dic[0]
        



