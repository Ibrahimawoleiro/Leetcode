class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        #Approach 1
        candidates = [num for num in range(1,10)]
        ans = []
        
        def helper(combination,total,curr_index):
            if total >= n:
                print(total)
                if total == n and len(combination) == k:  
                    ans.append(combination.copy())    
                return
            print(total,curr_index,)
            for index in range(curr_index,len(candidates)):
                current = total + candidates[index]
                combination.append(candidates[index])
                helper(combination,current,index+ 1)
                combination.pop()
                current -= candidates[index]
        helper([],0,0)

        return list(ans)