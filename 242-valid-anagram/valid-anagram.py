class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def freq(word, store):
            for l in word:
                if l in store:
                    store[l] += 1
                else:
                    store[l] = 1
        s_store = {}
        t_store = {}

        freq(s, s_store)
        freq(t, t_store)

        for l in s:
            if l not in t_store:
                return False
            if t_store[l] != s_store[l]:
                return False
        for l in t:
            if l not in s_store:
                return False
            if s_store[l] != t_store[l]:
                return False
        return True
        