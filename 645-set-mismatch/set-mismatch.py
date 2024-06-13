class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        store = {num + 1 for num in range(len(nums))}

        for num in nums:
            if num not in store:
                ans.append(num)
            else:
                store.remove(num)
                
        ans.append(store.pop())

        return ans