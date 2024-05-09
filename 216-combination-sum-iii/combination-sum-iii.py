class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = [i + 1 for i in range(9)]
        ans = []
        def helper(i,curr,s):
            if len(curr) == k or s >= n:
                if len(curr) == k and s == n:
                    ans.append(curr.copy())
                return
            
            for index in range(i , len(arr)):
                c_sum = s + arr[index]
                curr.append(arr[index])
                helper(index + 1, curr, c_sum)
                c_sum -= arr[index]
                curr.pop()

        helper(0, [], 0)
        return ans