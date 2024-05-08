class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = set()
        ans = set()
        for index in range(0,len(nums) - 2):
            if nums[index] in s:
                continue
            s.add(nums[index])
            l = index + 1
            r = len(nums) - 1
            while(l < r):
                curr = nums[index] + nums[l] + nums[r]
                if curr == 0:
                    ans.add((nums[index], nums[l], nums[r]))
                    l += 1
                elif curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
        return list(ans)
