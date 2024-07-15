class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse(start, end):
            if end <= 0:
                return
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        
        reverse(0, len(nums)  - 1)

        reverse(0, (k) % len(nums) - 1)
        reverse(k % len(nums), len(nums) - 1)
