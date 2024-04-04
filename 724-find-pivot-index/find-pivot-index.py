class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0 for val in range(len(nums))]
        postfix = [0 for val in range(len(nums))]

        i = 0
        total = nums[0]
        while(i < len(nums)):
            if i == 0:
                i+=1
                continue
            prefix[i] = total
            total+=nums[i]
            i+=1
        i-=1
        total = nums[i]
        while(i >= 0):
            if i == len(nums) - 1:
                i-=1
                continue
            postfix[i] = total
            total+= nums[i]
            i-=1
        i = 0
        while(i < len(nums)):
            if postfix[i] == prefix[i]:
                return i
            i+=1
        return -1
            
            