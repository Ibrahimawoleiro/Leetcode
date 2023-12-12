class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # #Approach1
        # checker = set()

        # for val in nums:
        #     if val in checker:
        #         return val
        #     checker.add(val) 


        # #Appraoch2
        # for val in range(len(nums)):
        #     if nums[abs(nums[val])] < 0:
        #        return abs(nums[val])
        #     nums[abs(nums[val])] *= -1
        
        #Approach3
        slow = nums[0]
        fast = nums[0]
        fast = nums[nums[fast]]
        slow = nums[slow]
        while(fast != slow):
            fast = nums[nums[fast]]
            slow = nums[slow]
        
        slow = nums[0]

        while(fast != slow):
            fast = nums[fast]
            slow = nums[slow]
        
        return fast



