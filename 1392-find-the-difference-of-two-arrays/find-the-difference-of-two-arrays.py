class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a_b = set(nums1)
        b_b = set(nums2)
        ans = []

        for val in nums1:
            if val in b_b:
                b_b.remove(val)
        
        for val in nums2:
            if val in a_b:
                a_b.remove(val)
        curr = []
        while a_b:
            curr.append(a_b.pop())
        ans.append(curr.copy())
        curr = []
        while b_b:
            curr.append(b_b.pop())
        ans.append(curr.copy())

        return ans