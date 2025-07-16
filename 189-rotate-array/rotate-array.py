class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k % len(nums) == 0:
            return

        rotation = k % len(nums)

        temp = []

        arr_length = len(nums)

        for i in range(arr_length - 1, arr_length - rotation - 1, - 1):

            temp.append(nums[i])
        
        for i in range(arr_length - rotation - 1, -1, -1):

            nums[i + rotation] = nums[i]
        
        j = 0

        for i in range(len(temp) - 1, - 1, -1):
            nums[j] = temp[i]
            j += 1 


