class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # #Appraoch1
        # result = []
        # checker = set()
        # for val in nums:
        #     if val in checker:
        #         result.append(val)
        #         continue
        #     checker.add(val)

        # return result

        #Approach2
        in_case = None
        result = []
        for index in range(len(nums)):
            if abs(nums[index]) < len(nums):
                if (nums[abs(nums[index])]) < 0:
                    result.append(abs(nums[index]))
                else:
                    nums[abs(nums[index])] *= -1
            
            else:
                if not in_case:
                    in_case = len(nums)
                else:
                    result.append(len(nums))
            
        return result