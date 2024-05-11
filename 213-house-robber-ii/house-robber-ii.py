class Solution:
    def rob(self, nums: List[int]) -> int:
        nums1 = nums[1:]
        nums2 = nums[:-1]
        print(nums1, nums2)
        dic1 = {}
        dic2 = {}
        def helper(i,numz,dic):
            if i >= len(numz):
                return 0

            if i in dic:
                return dic[i]
            m = 0
            for r in range(i+2, len(numz)):
                #right neighbor
                n = helper(r,numz, dic)
                if n > m:
                    m = n
            dic[i] = m + numz[i]

            return dic[i]

        #Edge cases: Length of arr == 1
        #            Length of arr == 2
        #            Length of arr == 3

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        return max(max(helper(0,nums1,dic1), helper(1,nums1,dic1)),max(helper(0,nums2,dic2), helper(1,nums2,dic2)))
        


        

