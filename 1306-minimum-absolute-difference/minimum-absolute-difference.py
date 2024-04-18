class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        i = 0
        j = 1
        min_diff = arr[j] - arr[i]
        while(j < len(arr)):
            if arr[j] - arr[i] < min_diff:
                min_diff = arr[j] - arr[i]
            i += 1
            j += 1
        i = 0
        j = 1
        ans = []
        while(j < len(arr)):
            if arr[j] - arr[i] == min_diff:
                ans.append([arr[i], arr[j]])
                i += 1
                j += 1
            else:
                i += 1
                j += 1
                
        return ans