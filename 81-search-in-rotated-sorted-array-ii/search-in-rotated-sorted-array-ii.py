class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def bs(s , e):
            left = s
            right = e
            ans = False
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return ans
        def rec(s, e):
            if s >= e:
                if s == e:
                    if nums[s] == target:
                        return True
                else:
                    return False
            mid = (s + e) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[s] and target >= nums[s] and target < nums[mid]:
                return bs(s,mid - 1)
            elif nums[mid] < nums[e] and target > nums[mid] and target <= nums[e]:
                return bs(mid+ 1, e)
            else:
                left = rec(s, mid - 1)
                right = rec(mid + 1, e)
                if left != False:
                    return left
                return right
        return rec(0,len(nums) - 1)