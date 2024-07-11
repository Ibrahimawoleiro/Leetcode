class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        store = {}

        ans = []

        for num in nums:
            if num in store:
                store[num] += 1
            else:
                store[num] = 1

            if store[num] <= len(ans):
                ans[store[num] - 1].append(num)

            else:
                ans.append([])
                ans[store[num] - 1].append(num)

        return ans
        