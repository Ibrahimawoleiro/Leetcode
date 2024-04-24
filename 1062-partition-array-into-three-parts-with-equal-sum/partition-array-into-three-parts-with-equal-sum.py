class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        count = 3
        sub_sum = total/3
        checker = sub_sum
        for index in range(len(arr)):
            checker -= arr[index]
            if checker == 0:
                count -= 1
                checker = sub_sum
            
        
        return count <= 0