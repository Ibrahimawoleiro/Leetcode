class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        def bs(left, right):

            while left <= right:

                mid = (left + right) // 2

                if nums[mid] == target:

                    return True

                elif nums[mid] > target:

                    right = mid - 1

                else:

                    left = mid + 1
            
            return False

        low = 0

        high = len(nums) - 1

        def isPresent(l, r):

            if l > r:
                return False

            mid = (l + r) // 2

            if nums[mid] == target:

                return True

            elif nums[mid] > nums[l]:

                result = bs(l, mid)

                if result:

                    return result

            elif nums[mid] < nums[r]:

                result = bs(mid + 1, r)

                if result:

                    return result

                result =  isPresent(l, mid - 1)

                if result:
                    return result
            
            result =  isPresent(mid + 1, r)

            if result:
                return result

            return isPresent(l, mid - 1)
        
        return isPresent(low, high)