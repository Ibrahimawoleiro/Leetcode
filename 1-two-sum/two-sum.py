class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        store = {}

        for index in range(len(nums)):
            if (target - nums[index] )in store:
                return [store[target - nums[index]], index]

            store[nums[index]] = index

        return []