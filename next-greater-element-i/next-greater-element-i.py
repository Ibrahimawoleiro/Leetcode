class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in range(len(nums1)):
            right_greater = -1
            seen = False
            for number in range(len(nums2)):
                if nums2[number] == nums1[num]:
                    seen = True
                    continue
                if nums2[number] > nums1[num] and seen:
                    right_greater = nums2[number]
                    break
            ans.append(right_greater)
        return ans
        