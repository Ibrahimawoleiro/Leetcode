class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) -1 
        low  = 0

        while(low<=high):
            mid = int((low + high)/2)
            print(mid, low, high)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1