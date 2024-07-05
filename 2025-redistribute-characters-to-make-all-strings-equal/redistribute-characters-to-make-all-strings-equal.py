class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1:
            return True
        store = {}
        for arr in words:
            for l in arr:
                if l in store:
                    store[l] += 1
                else:
                    store[l] = 1
        for (key, val) in store.items():
            if val % len(words) > 0:
                return False
        return True