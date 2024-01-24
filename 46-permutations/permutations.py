class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    #I need an empty array to store the overall output
    #I need an empty array to store the current permutation i am making

        array = []

        def helper(arr,permutation):
            if len(permutation) == len(nums):
                array.append(permutation.copy())
                return
            for index in range(len(arr)):
                permutation.append(arr.pop(0)) 
                helper(arr,permutation)
                arr.append(permutation.pop())
        helper(nums.copy(),[])

        return array
            





        
