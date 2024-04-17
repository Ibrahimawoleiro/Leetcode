class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        j = 0
        ans = []
        while(j < len(arr)):
            if arr[j] == 0:
                ans.append(0)
                if len(ans) == len(arr):
                    j+=1
                    break
                ans.append(0)
                j+=1
            else:
                ans.append(arr[j])
                j+=1
            
        for index in range(len(arr)):
            arr[index] = ans[index]