class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        def helper(i,curr, s):
            if s >= target:
                if s == target:
                    ans.add(tuple(curr.copy()))
                return 
            
            for index in range(i , len(candidates)):
                current = s + candidates[index]
                curr.append(candidates[index])

                helper(index, curr, current)
                curr.pop()
                current -= candidates[index]

        helper(0,[],0)
        return ans