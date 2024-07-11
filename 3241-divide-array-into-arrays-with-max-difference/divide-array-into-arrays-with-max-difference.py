class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        nums.sort()

        j = 2

        while j < len(nums):

            if nums[j] - nums[j - 2] > k:
                return []

            j += 3
        ans = []

        j = 2

        while j < len(nums):

            ans.append(nums[j-2:j+1])

            j += 3
        return ans