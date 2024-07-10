class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        

        prefix = []

        for index in range(len(nums)):
            if index > 0:
                prefix.append(nums[index] + prefix[index - 1])
            else:
                prefix.append(nums[index])

        ans = [0 for num in range(len(nums))]

        for index in range(len(nums)):

            left_count = index - 0
            right_count = len(nums) - 1 - index

            left = abs(prefix[index - 1] - (left_count * nums[index])) if index > 0 else 0
            right = abs((prefix[len(nums) - 1] - prefix[index]) - (right_count * nums[index]))

            ans[index] = left + right

        return ans
