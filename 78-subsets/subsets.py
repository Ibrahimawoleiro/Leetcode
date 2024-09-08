class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for val in range((1 << len(nums) )):
            list = []
            for index in range(len(nums)):
                if val & (1 << index) > 0:
                    list.append(nums[index])
            ans.append(list[::-1])

        return ans