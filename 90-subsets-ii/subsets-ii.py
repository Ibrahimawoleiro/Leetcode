class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        def rec(arr, combo,ans, i):
            if i >= len(arr):
                return
            for index in range(i , len(arr)):
                if index > i and arr[index] == arr[index - 1]:
                    continue
                combo.append(arr[index])
                ans.append(combo.copy())
                rec(arr, combo,ans, index + 1)
                combo.pop()
        rec(nums, [], ans, 0)
        return ans