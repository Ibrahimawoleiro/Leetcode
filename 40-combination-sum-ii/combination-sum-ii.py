class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        print(len(candidates))
        #Approach 1
        candidates.sort()
        ans = []
        def helper(combination,total,curr_index):
            if total >= target:
                if total == target:
                    ans.append(combination.copy())    
                return
            dp = set()
            for index in range(curr_index,len(candidates)):
                if candidates[index] in dp:
                    continue
                dp.add(candidates[index])
                current = total + candidates[index]
                combination.append(candidates[index])
                helper(combination,current,index+ 1)
                combination.pop()
                current -= candidates[index]
        helper([],0,0)

        return list(ans)