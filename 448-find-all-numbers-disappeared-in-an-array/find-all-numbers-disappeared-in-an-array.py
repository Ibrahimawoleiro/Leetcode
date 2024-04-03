class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for index in range(len(nums)):
            if nums[abs(nums[index]) - 1] > 0:
                nums[abs(nums[index]) - 1] *= -1

        for index in range(len(nums)):
            if nums[index] > 0:
                ans.append(index + 1)

        return ans