class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def min_finder(s, e):
            if s > e:
                return nums[s]
            if s == e:
                return nums[s]
            
            mid = (s + e) // 2
            #Greater than both ends
            if mid == s:
                return min(nums[mid], min_finder(mid+1 , e))
            if nums[mid] > nums[s] and nums[mid] > nums[e]:
                return min(nums[mid],min_finder(mid + 1, e))
            #Less than both ends
            elif nums[mid] < nums[s] and nums[mid] < nums[e]:
                return min(nums[mid], min_finder(s , mid-1))
            #Less than one end
            else:
                return min_finder(s , mid - 1)

        return min_finder(0 , len(nums) - 1)