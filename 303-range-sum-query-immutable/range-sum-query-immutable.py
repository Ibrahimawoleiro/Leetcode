class NumArray:
    #Approach1
    # def __init__(self, nums: List[int]):
    #     self.nums = nums

    # def sumRange(self, left: int, right: int) -> int:
    #     sum = 0
    #     while(left <= right):
    #         sum += self.nums[left]
    #         left+=1
    #     return sum

    # #Approach 2
    # def __init__(self, nums: List[int]):
    #     self.nums = nums
    #     self.ans = [[0 for val in range(len(nums))] for val in range(len(nums))]
    #     for index in range(len(nums)):
    #         sum = 0
    #         for right_of_index in range(index,len(nums)):
    #             sum+= nums[right_of_index]
    #             self.ans[index][right_of_index] = sum    

    # def sumRange(self, left: int, right: int) -> int:
    #     return self.ans[left][right]

    #Approach 3
    def __init__(self, nums: List[int]):
         self.nums = nums
         for val in range(len(nums)):
            if val == 0:
                continue
            nums[val] = nums[val] + nums[val - 1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        else:
            return self.nums[right] - self.nums[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
#     def __init__(self, nums: List[int]):
#         self.nums = nums

#     def sumRange(self, left: int, right: int) -> int:
#         while()
# param_1 = obj.sumRange(left,right)