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
            elif count > 0 and index == len(arr) - 1:
                return False
        
        return count <= 0