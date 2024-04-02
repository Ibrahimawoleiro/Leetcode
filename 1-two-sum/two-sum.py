class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # #1
        # dic = {}
        # for index in range(len(nums)):
        #     if target - nums[index] in dic:
        #         return [dic[target-nums[index]], index]
        #     dic[nums[index]] = index

        #2
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]