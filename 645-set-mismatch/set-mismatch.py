class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        for index in range(len(nums)):
            if nums[abs(nums[index]) - 1] < 0:
                ans.append(abs(nums[index]))
            else:
                nums[abs(nums[index]) - 1] *= -1

        for index in range(len(nums)):
            if nums[index] > 0:
                ans.append(index + 1)

        return ans