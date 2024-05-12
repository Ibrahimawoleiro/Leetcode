class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        def helper(arr):
            
            if len(arr) == 0:
                return 0

            zero_count = 0
            zero_indexes = []
            negative_count = 0
            negative_indexes = []

            for index in range(len(arr)):
                if arr[index] == 0:
                    zero_count += 1
                    zero_indexes.append(index)
                if arr[index] < 0:
                    negative_count += 1
                    negative_indexes.append(index)
            if zero_count == 0 and negative_count % 2 == 0:
                curr = 1
                for num in arr:
                    curr *= num
                return curr
            
            elif zero_count == 0 and negative_count % 2 == 1:

                if len(arr) == 1:
                    return arr[0]

                l = 0
                r = len(arr) - 1

                while(l < len(arr)):
                    if arr[l] < 0:
                        break
                    l+=1
                
                while(r>= 0):
                    if arr[r] < 0:
                        break
                    r -= 1
                
                left = helper(arr[0: r])
                right = helper(arr[l + 1: len(arr)])
                return max(left, right)
                
            elif zero_count > 0:
                max_from_subs = 0
                start = 0
                for end in zero_indexes:
                    m = helper(arr[start: end])
                    if m > max_from_subs:
                        max_from_subs = m
                    start = end + 1
                m = helper(arr[start:len(arr)])
                if m > max_from_subs:
                    max_from_subs = m
                return max_from_subs
        return helper(nums)