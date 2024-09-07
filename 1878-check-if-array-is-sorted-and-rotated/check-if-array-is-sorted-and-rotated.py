class Solution:
    def check(self, nums: List[int]) -> bool:
        def is_sorted(s, e):
            for index in range(s, e + 1):
                if index == s:
                    continue
                if nums[index] < nums[index - 1]:
                    return False

            return True
        rotation_index = len(nums)
        for i in range(len(nums)):
            if i == 0:
                continue
            if nums[i] < nums[i - 1]:
                rotation_index = i
                break
        left = True
        right = True
        if rotation_index < len(nums):
            left = is_sorted(0, rotation_index - 1)
            right = is_sorted(rotation_index, len(nums) - 1)
            if left and right:
                if nums[-1] <= nums[0]:
                    return True
            return False
        return True