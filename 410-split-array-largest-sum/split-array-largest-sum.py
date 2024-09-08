class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        #code here
        n = len(nums)
        m = k
        arr = nums
        if (m > n):
            return -1
        mini_allocation = max(arr)
        max_allocation = sum(arr)
        ans = float('inf')
        while mini_allocation<= max_allocation:
            allocation = (mini_allocation + max_allocation) // 2
            curr_allocation = 0
            student_count = 1
            max_student_allocation = 0
            for page_count in arr:
                if page_count + curr_allocation <= allocation:
                    curr_allocation += page_count
                else:
                    curr_allocation = page_count
                    student_count += 1
                max_student_allocation = max(curr_allocation, max_student_allocation)
            if student_count <= m:
                ans = min(max_student_allocation, ans)
                max_allocation = allocation - 1
            else:
                mini_allocation = allocation + 1
        return ans if ans < 10 ** 10 else -1