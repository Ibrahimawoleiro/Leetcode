class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    #I need an empty array to store the overall output
    #I need an empty array to store the current permutation i am making

        array = []

        def helper(arr,permutation):
            if len(permutation) == len(nums):
                print(permutation,"ghbjkl")
                array.append(permutation.copy())
                return
            print('permutaion',len(permutation), 'nums', len(nums))
            for index in range(len(arr)):
                print(arr,"arr")
                permutation.append(arr.pop(0))
                print(permutation,"permutation")
                helper(arr,permutation)
                arr.append(permutation.pop())

        helper(nums.copy(),[])

        return array
            





        
