class Solution:
    def canJump(self, nums: List[int]) -> bool:
        energy = 1
        for i in range(len(nums)):
            energy -= 1
            energy = max(energy, nums[i])
            if i + energy >= len(nums) - 1:
                return True
            if energy == 0:
                return False
        
        return False