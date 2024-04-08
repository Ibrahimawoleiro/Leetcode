class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        checker = k
        current = 1
        kth_missing = -1
        runner = 0
        while(checker > 0 and runner < len(arr)):
            if arr[runner] != current:
                kth_missing = current
                current += 1
                checker -= 1
            else:
                current += 1
                runner += 1
        
        if checker > 0:
            return arr[-1] + checker
            
        return kth_missing