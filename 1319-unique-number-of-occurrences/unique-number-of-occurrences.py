class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        store = collections.Counter(arr)
        checker = set()
        for key, value in store.items():
            if value in checker:
                return False
            checker.add(value)
        return True