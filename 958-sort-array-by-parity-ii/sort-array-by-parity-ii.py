class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for val in nums:
            if val % 2 == 0:
                even.append(val)
            else:
                odd.append(val)

        ans = []
        i = 0
        j = 0
        while(i < len(even) or j < len(odd)):
            if i <= j:
                ans.append(even[i])
                i+=1
            else:
                ans.append(odd[j])
                j+=1
        
        return ans