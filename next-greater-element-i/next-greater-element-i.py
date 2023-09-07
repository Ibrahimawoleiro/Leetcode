class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in range(len(nums1)):
            index = -1
            seen = False
            for number in range(len(nums2)):
                if nums2[number] == nums1[num]:
                    seen = True
                    continue
                if nums2[number] > nums1[num] and seen:
                    index = nums2[number]
                    break
            ans.append(index)
        return ans
        