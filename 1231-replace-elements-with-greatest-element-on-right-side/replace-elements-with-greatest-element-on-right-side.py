class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [ 0 for num in range(len(arr))]
        m = -1
        for index in range(len(arr) - 1, -1, -1):
            if index == len(arr) - 1:
                ans[index] = m
                m = arr[index]
                continue
            
            ans[index] = m

            m = max(arr[index], m)

        return ans