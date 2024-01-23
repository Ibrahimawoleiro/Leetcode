class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]
        def helper(checker,index):
            if index > len(nums) - 1:
                return
            checker.append(nums[index])
            arr.append(checker.copy())
            index += 1
            while(index < len(nums)):
                helper(checker,index)
                checker.pop()
                index += 1
            
            
        for index in range(len(nums)):
            helper([],index)

        return arr