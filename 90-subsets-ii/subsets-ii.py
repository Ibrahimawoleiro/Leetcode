class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Approach 1
        nums.sort()
        arr = set([()])
        def helper(checker,index):
            if index > len(nums) - 1:
                return
            checker.append(nums[index])
            arr.add(tuple(checker.copy()))
            index += 1
            while(index < len(nums)):
                helper(checker,index)
                checker.pop()
                index += 1
            
            
        for index in range(len(nums)):
            helper([],index)

        return list(arr)