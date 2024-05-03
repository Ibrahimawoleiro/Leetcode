class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def helper(low, high):
            if low >= high:
                return 
            
            mid = (low + high) // 2

            helper(low, mid)

            helper(mid + 1, high)

            left_iterator = 0

            right_iterator = 0

            main_iterator = low

            left_arr = nums[low: mid + 1]

            right_arr = nums[mid + 1: high + 1]
            while(left_iterator < len(left_arr) or right_iterator < len(right_arr)):
                if left_iterator < len(left_arr) and right_iterator < len(right_arr):
                    if left_arr[left_iterator] < right_arr[right_iterator]:
                        nums[main_iterator] = left_arr[left_iterator]
                        main_iterator += 1
                        left_iterator += 1
                    else:
                        nums[main_iterator] = right_arr[right_iterator]
                        main_iterator += 1
                        right_iterator += 1
                elif left_iterator < len(left_arr):
                    nums[main_iterator: high + 1] = left_arr[left_iterator: len(left_arr)]
                    break
                else:
                    nums[main_iterator: high + 1] = right_arr[right_iterator: len(right_arr)]
                    break
        helper(0, len(nums) - 1)
        return nums

