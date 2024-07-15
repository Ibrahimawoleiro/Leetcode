class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        ans = [0 for num in nums]

        ans_iterator = 0

        left = 0

        right = len(nums) - 1

        high_active = True

        while left <= right:

            if high_active:
                ans[ans_iterator] = nums[right]
                right -= 1
                high_active = False
                ans_iterator += 1
            else:
                ans[ans_iterator] = nums[left]
                left += 1
                high_active = True
                ans_iterator += 1

        return ans
