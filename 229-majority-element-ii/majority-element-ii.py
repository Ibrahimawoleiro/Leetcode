class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        store = {}
        ans = []
        for num in nums:
            if num in store:
                store[num]+=1
            else:
                store[num] = 1

        checker = len(nums) // 3

        for key, val in store.items():
            if val > checker:
                ans.append(key)
        
        return ans
        