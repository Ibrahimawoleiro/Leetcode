class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [0 for val in range(len(nums))]
        front = 0
        back = len(nums) - 1
        arr_pointer = len(nums) - 1
        while(arr_pointer >= 0):
            if nums[front] ** 2 >= nums[back] ** 2:
                arr[arr_pointer] = nums[front] ** 2
                front+=1
            else:
                arr[arr_pointer] = nums[back] ** 2
                back-=1
            arr_pointer -=1

        return arr
                