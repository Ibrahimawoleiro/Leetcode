class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #Approach 1
        array = set()

        def helper(arr,permutation):
            if len(permutation) == len(nums):
                array.add(tuple(permutation.copy()))
                return
            for index in range(len(arr)):
                permutation.append(arr.pop(0)) 
                helper(arr,permutation)
                arr.append(permutation.pop())
        helper(nums.copy(),[])

        return list(array)
            