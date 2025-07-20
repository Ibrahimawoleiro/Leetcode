class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        ans = [5001]

        def findMin(low, high):
            if low > high:
                return 

            mid = (low + high) // 2

            if nums[mid] >= nums[low]:

                ans[0] = min (ans[0], nums[low])

                return findMin(mid + 1, high)

            ans[0] = min(nums[mid], ans[0])

            return findMin(low, mid - 1)

        findMin(0 , len(nums) - 1)

        return ans[0]