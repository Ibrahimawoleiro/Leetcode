class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i+1 for i in range(n)]
        ans = []
        def helper(i,curr):
            if len(curr) == k:
                ans.append(curr.copy())
                return
            for index in range(i,len(arr)):
                curr.append(arr[index])
                helper(index+1, curr)
                curr.pop()

        helper(0, [])

        return ans
            