class Solution:
    def search(self, nums: List[int], target: int) -> bool:
          #Binary Search
        def bs(s, e):
            while(s<= e):
                mid = (s + e)// 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    e = mid - 1
                else:
                    s = mid + 1
            return False

        def rec(s, e):
            
            if s > e:
                return False
            
            mid = (s + e)//2

            if nums[mid] == target:
                return True
            #If the target might be located in the sorted part
            if nums[mid] < nums[e] and target <= nums[e] and target >= nums[mid]:
                return bs(mid + 1, e)
            if nums[mid] > nums[s] and target >= nums[s] and target < nums[mid]:
                return bs(s, mid - 1)
            #If the target might be located in one of the unsorted part
            left_unsorted = False
            if nums[mid] <= nums[s] and (target < nums[mid] or target >= nums[s]):
                left_unsorted =  rec(s, mid - 1)
            if left_unsorted:
                return True
            
            if nums[mid] >= nums[e] and (target <= nums[e] or target > nums[mid]):
                return rec(mid + 1, e)

            return False
        return rec(0, len(nums) - 1)