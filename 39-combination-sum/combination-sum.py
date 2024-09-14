class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def rec(arr, rem, combo, i,ans):
            if i >= len(arr) or  rem == 0:
                if rem == 0:
                    ans.append(combo.copy())
                return 
            if rem >= arr[i]:
                combo.append(arr[i])
                rec(arr, rem - arr[i], combo, i, ans)
                combo.pop()
            rec(arr, rem, combo, i + 1, ans)
        rec(candidates, target, [], 0, ans)
        return ans