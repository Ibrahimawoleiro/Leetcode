class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        candidates.sort()
        def helper(i,curr, s):
            if s >= target:
                if s == target:
                    ans.add(tuple(curr.copy()))
                return 
            dp = set()
            for index in range(i , len(candidates)):
                if candidates[index] in dp:
                    continue
                dp.add(candidates[index])
                current = s + candidates[index]
                curr.append(candidates[index])
                helper(index + 1, curr, current)
                curr.pop()
                current -= candidates[index]

        helper(0,[],0)
        return ans