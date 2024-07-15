class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n_arr = []
        p_arr = []
        ans = []
        for number in nums:
            if number > 0:
                p_arr.append(number)
            else:
                n_arr.append(number)

        
        i = 0
        
        while i < len(p_arr):
            ans.extend([p_arr[i], n_arr[i]])
            i += 1

        return ans