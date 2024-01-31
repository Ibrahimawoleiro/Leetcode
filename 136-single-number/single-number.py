class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # #Approach 1
        # checker = set()
        # for val in nums:
        #     if val not in checker:
        #         checker.add(val)
        #     else:
        #         checker.remove(val)
        
        # return checker.pop()

        # #Approach 2
        
        # for index in range(len(nums)):
        #     count = 0
        #     for checker in range(len(nums)):
        #         if index == checker:
        #             continue
                
        #         if nums[checker] == nums[index]:
        #             count+=1

        #         if count > 0:
        #             break
        #     if count == 0:
        #         return nums[index]

        # #Approach 3

        res = 0
        for n in nums:
            res = n ^ res
        return res


