class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        store = collections.Counter(nums)
        for key, val in store.items():
            if val == len(nums) / 2:
                return key
        return 0