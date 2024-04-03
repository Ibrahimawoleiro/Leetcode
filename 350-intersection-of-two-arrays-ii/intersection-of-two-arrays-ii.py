class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #1
        store = {}
        ans = []
        for val in nums1:
            if val not in store:
                store[val]  = 1
            else:
                store[val] += 1
        
        for val in nums2:
            if val in store:
                ans.append(val)
                store[val] -= 1
                if store[val] == 0:
                    del store[val]
        return ans