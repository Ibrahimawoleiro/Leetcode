class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        curr_range = ''
        ans = []
        i = 0
        j = 0
        while(j < len(nums)):
            print(i,'i',j,'j')
            if i == j:
                curr_range += str(nums[i])
                j+=1
                continue
            elif nums[j] - nums[i] > 1:
                if curr_range != str(nums[i]):
                    curr_range+= f'->{str(nums[i])}'
                ans.append(curr_range)
                curr_range = ''
                i+=1
                continue
            i+=1
            j+=1

        if len(curr_range) > 0:
            if str(nums[-1]) != (curr_range):
                curr_range+=f'->{nums[-1]}'
                ans.append(curr_range)
            else:
                ans.append(curr_range)
        
        return ans