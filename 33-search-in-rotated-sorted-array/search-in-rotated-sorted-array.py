class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(s, e):
            while(s<= e):
                mid = (s + e)// 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    e = mid - 1
                else:
                    s = mid + 1
            return -1

        def rec(s, e):
            print(s,e)
            
            if s > e:
                return -1
            
            mid = (s + e)//2

            if nums[mid] == target:
                return mid
            print(nums[s],nums[mid], nums[e])
            print()
            #If the target might be located in the sorted part
            if nums[mid] < nums[e] and target <= nums[e] and target >= nums[mid]:
                return bs(mid + 1, e)
            elif nums[mid] > nums[s] and target >= nums[s] and target < nums[mid]:
                print('k')
                return bs(s, mid - 1)
            #If the target might be located in one of the unsorted part
            elif nums[mid] < nums[s] and (target < nums[mid] or target >= nums[s]):
                return rec(s, mid - 1)
            elif nums[mid] > nums[e] and (target <= nums[e] or target > nums[mid]):
                return rec(mid + 1, e)
            return -1
        return rec(0, len(nums) - 1)
            
