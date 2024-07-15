class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        ans = 0
        nums.sort()
        for index in range(len(nums)):
            if nums[index] * 2 > target:
                continue
            
            low = index

            high = len(nums) - 1

            i = -1

            while(low <= high):

                mid = (low + high ) // 2
                
                if nums[mid] + nums[index] > target:
                    high = mid - 1

                else:
                    i = mid
                    low = mid + 1

            
            ans += 2 ** (i - index)
            
        return ans % (10 ** 9 + 7)