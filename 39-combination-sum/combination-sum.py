class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()

        def helper(combination,total):
            if total >= target:
                if total == target:
                    ans.add(tuple(sorted(combination.copy())))       
                return

            for index in range(len(candidates)):
                current = total + candidates[index]
                combination.append(candidates[index])
                helper(combination,current)
                combination.pop()
                current -= candidates[index]
            
        helper([],0)

        return list(ans)

