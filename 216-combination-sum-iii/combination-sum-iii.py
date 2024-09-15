class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # K is the size of each subarray
        # N is the target sum
        nums = [number for number in range(1, 10)]
        ans = []
        def rec(combo, rem, i):
            if rem == 0 or i >= len(nums):
                if rem == 0 and len(combo) == k:
                    ans.append(combo.copy())
                return
            #take 
            if rem >= nums[i]:
                combo.append(nums[i])
                rec(combo, rem - nums[i], i + 1)
                combo.pop()
            #Don't take
            rec(combo, rem , i + 1)
        rec([], n, 0)
        return ans
