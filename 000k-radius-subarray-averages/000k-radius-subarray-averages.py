class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        """
        create an array called ans with same length as nums and all values initialized to -1
        check if 2*k is greater than nums length
        if yes, return ans
        if no, for every index in nums, sum all elements before it and current index, then put it in current index
        for every element starting from k to n-1-k called runner
            if runner = k
                window_sum = nums[runner+k]
                ans[runner] = math.floor(window_sum/2*k+1)
                continue
            window_sum = nums[runner+k] - nums[runner-k-1]
            ans[runner] = math.floor(window_sum/2*k+1)
            
        return ans
        """
        ans = [-1 for num in nums]
        
        if 2 * k > len(nums):
            return ans
        for index in range(len(nums)):
            if index == 0:
                continue
            nums[index]= nums[index]+nums[index-1]
            
        runner = k
        
        while(runner + k < len(nums)):
            print(runner)
            if runner == k:
                window_sum = nums[runner+k]
                ans[runner] = math.floor(window_sum/(2*k+1))
                runner+=1
                continue
            window_sum = nums[runner+k] - nums[runner-k-1]
            ans[runner] = math.floor(window_sum/(2*k+1))
            runner+=1
        return ans
            
        