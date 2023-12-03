class NumArray:
    #Approach1
    # def __init__(self, nums: List[int]):
    #     self.nums = nums

    # def sumRange(self, left: int, right: int) -> int:
    #     total = 0
    #     while(left <= right):
    #         total+=self.nums[left]
    #         left += 1
    #     return total
    
    # #This gives a memory limit Exceeded
    # def __init__(self, nums: List[int]):
    #     self.dictionary = {}
    #     for num in range(len(nums)):
    #         for val in range(len(nums)):
    #             if((num,val) in self.dictionary):
    #                 continue
    #             elif num == val:
    #                 self.dictionary[(num,val)] = nums[num]
    #             else:
    #                 curr = self.dictionary[(num,val-1)] + nums[val]
    #                 self.dictionary[(val,num)] = curr
    #                 self.dictionary[(num,val)] = curr

    # def sumRange(self, left: int, right: int) -> int:
    #     return self.dictionary[(left,right)]

    #Approach3
    def __init__(self, nums: List[int]):
        self.nums = nums
        for val in range(len(self.nums)):
            if val == 0:
                continue
            self.nums[val] = self.nums[val - 1] + self.nums[val]
        
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        return self.nums[right] - self.nums[left - 1]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

        
