class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0

        store = {}
        helper = nums.copy()

        for index in range(len(helper)):
            if helper[index] == 0:
                helper[index] = -1

        for index in range(len(nums)):
            if index == 0:
                continue
            helper[index] = helper[index] + helper[index - 1]

        ans = 0
        # print(helper)

        for index in range(len(helper)):
            if helper[index] not in store:
                store[helper[index]] = index
            elif helper[index] in store:
                if index - store[helper[index]] > ans:
                    ans = index - store[helper[index]]
            if helper[index] == 0:
                if (index - 0) + 1> ans:
                    ans = index + 1
        return ans