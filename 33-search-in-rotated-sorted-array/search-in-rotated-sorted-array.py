class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        def bs(l, r):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        def rec(l , r):
            if l >= r:
                if nums[l] == target:
                    return l
                return -1
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[l]:
                bs_search = bs(l, mid - 1)
                if bs_search != -1:
                    return bs_search
                return rec(mid + 1, r)
            else:
                bs_search = bs(mid + 1 , r)
                if bs_search != -1:
                    return bs_search
                return rec(l , mid - 1)

        return rec(0, n)