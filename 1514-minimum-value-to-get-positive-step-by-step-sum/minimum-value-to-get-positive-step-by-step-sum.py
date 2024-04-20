class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [0 for v in nums]
        prefix[0] = nums[0]
        i = 0
        last = nums[0]
        while(i < len(nums)):
            if i == 0:
                i+=1
                continue
            last+=nums[i]
            prefix[i] = last
            i+=1
        smallest = min(prefix)
        if smallest > 0:
            return 1
        print(prefix)
        return -1 * smallest + 1

