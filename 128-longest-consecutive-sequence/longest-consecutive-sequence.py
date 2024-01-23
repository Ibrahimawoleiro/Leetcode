class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Approach 1
        if len(nums) == 0:
            return 0

        curr_count = 1
        max_count = 1
        seen = set()
        for val in nums:
            seen.add(val)
        ans = list(seen)
        ans.sort()
        for index in range(len(ans)):
            if index == 0:
                continue
            if ans[index] - ans[index - 1] == 1 :
                curr_count+=1
                if curr_count > max_count:
                    max_count = curr_count
            else:
                curr_count = 1
        
        return max_count
            