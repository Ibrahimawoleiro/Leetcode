from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        store = set()

        print(nums)
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the first number
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates for the second number
                    continue

                l = j + 1
                k = len(nums) - 1

                while l < k:
                    total = nums[i] + nums[j] + nums[l] + nums[k]
                    if total == target:
                        store.add((nums[i], nums[j], nums[l], nums[k]))
                        while l < k and nums[l] == nums[l + 1]:  # Skip duplicates for the third number
                            l += 1
                        while l < k and nums[k] == nums[k - 1]:  # Skip duplicates for the fourth number
                            k -= 1
                        l += 1
                        k -= 1
                    elif total > target:
                        k -= 1
                    else:
                        l += 1

        return [list(quad) for quad in store]
