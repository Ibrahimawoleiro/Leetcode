class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        trial = 1

        for index in range(len(nums) - 1):
            if nums[index] > nums[index + 1]:
                if trial > 0:
                    trial -= 1
                    if index == 0:
                        nums[index] = nums[index + 1]
                        continue
                    else:
                        if nums[index - 1] > nums[index + 1]:
                            nums[index + 1] = nums[index]
                            continue
                        else:
                            nums[index] = nums[index + 1]
                else:
                    return False

        return True