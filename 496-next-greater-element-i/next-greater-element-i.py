class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        store = {}
        ans = []
        for val in nums2[::-1]:
            if len(stack) == 0:
                stack.append(val)
                store[val] = -1
            else:
                while(stack and stack[-1] < val):
                    stack.pop()
                
                if stack:
                    store[val] = stack[-1]
                else:
                    store[val] = -1
                stack.append(val)
        
        for val in nums1:
            ans.append(store[val])

        return ans