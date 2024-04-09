class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        start = 0
        end = 0
        count = 1
        maximum_count = 1
        while end < len(nums):
            if start == end:
                end+=1
                continue
            if nums[end] > nums[start]:
                print(nums[start], nums[end])
                count+=1
                if count > maximum_count:
                    print(count)
                    maximum_count = count
                end+=1
                start+=1
            else:
                count = 1
                start = end

        return maximum_count
