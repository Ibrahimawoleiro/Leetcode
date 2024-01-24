class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr  = [number for number in range(1,n+1)]
        
        ans = []

        def helper(curr_index,combination):
            if len(combination) == k:
                ans.append(combination.copy())
                return
            
            for index in range(curr_index, len(arr)):
                combination.append(arr[index])
                helper(index + 1, combination)
                combination.pop()

        helper(0,[])
        return ans
            
