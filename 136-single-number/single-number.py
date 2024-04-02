class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # #1
        # s = set()
        # for val in nums:
        #     if val not in s:
        #         s.add(val)
        #     else:
        #         s.remove(val)
        # return s.pop()

        #2
        curr = nums[0]
        for val in range(1, len(nums)):
            curr = curr ^ nums[val]

        return curr
