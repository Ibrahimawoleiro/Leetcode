class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index in range(len(nums)):
            if target - nums[index] in dic:
                return [dic[target-nums[index]], index]
            dic[nums[index]] = index