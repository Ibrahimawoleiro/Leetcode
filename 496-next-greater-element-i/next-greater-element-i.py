class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        store = {}

        stack = []

        ans = []

        for num in nums1:
            store[num] = -1

        for index in range(len(nums2) - 1, -1, -1):

            while stack and stack[-1] <= nums2[index]:
                stack.pop()  

            if stack:
                if nums2[index] in store:
                    store[nums2[index]] = stack[-1]
            else:
                if nums2[index] in store:
                    store[nums2[index]] = -1
            stack.append(nums2[index])

        for index in range(len(nums1)):
            ans.append(store[nums1[index]])

        return ans