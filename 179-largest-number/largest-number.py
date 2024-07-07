class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        for index in range(len(nums)):
            nums[index]  = str(nums[index])
        winner = 0
        for index in range(len(nums) - 1):
            left = nums[index]
            for check in range(index + 1, len(nums)):
                right = nums[check]

                left_right = left+right

                right_left = right + left

                if int(left_right) == int(right_left):
                    if len(left) < len(right):
                        continue
                    else:
                        nums[index], nums[check] = nums[check], nums[index]
                elif int(left_right) > int(right_left):
                    continue
                else:
                    nums[index], nums[check] = nums[check], nums[index]
                    left = nums[index]

        if nums[0] == '0':
            return '0'
        return ''.join(nums)