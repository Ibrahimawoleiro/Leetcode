class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # #Approach1
        ans = [0 for val in nums]
        ans_pointer = len(ans) - 1

        front = 0
        back = len(nums) - 1

        while(front <= back):
            if(nums[front] ** 2 > nums[back] ** 2):
                ans[ans_pointer] = nums[front] ** 2
                ans_pointer -=1
                front += 1
            else:
                ans[ans_pointer] = nums[back] ** 2
                ans_pointer -= 1
                back -= 1
            
        return ans


                