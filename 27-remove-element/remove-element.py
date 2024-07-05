class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = 0
        i = 0
        j = len(nums) - 1

        while i <=j:
            if nums[i] != val:
                count += 1
                i+= 1
            else:
                while(j>= i and nums[j] == val):
                    j -= 1
                if i < j and nums[i] == val and nums[j] != val:
                    nums[i], nums[j] = nums[j], nums[i]
        return count