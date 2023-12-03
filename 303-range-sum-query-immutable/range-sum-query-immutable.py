class NumArray:
    #Approach1
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        while(left <= right):
            total+=self.nums[left]
            left += 1
        return total



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# def __init__(self, nums: List[int]):
        

#  def sumRange(self, left: int, right: int) -> int:
        
