class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        seen.add(())
        for index in range(len(nums)):
            print(index,'jjjj')
            self.helper(index, seen, nums, [])

        return list(seen)
        
    def helper(self, index, seen, nums, curr):
        if index >= len(nums):
            return 
        curr.append(nums[index])
        print(curr)
        seen.add(tuple(curr))
        if index <= len(nums) - 1:
            for k in range((len(nums) - 1) - index):
                self.helper(index+k+1, seen, nums, curr)
                print(k,'now')
                print(curr)
                curr.pop()
                print(curr,'after')
                
        else:
            curr.pop()