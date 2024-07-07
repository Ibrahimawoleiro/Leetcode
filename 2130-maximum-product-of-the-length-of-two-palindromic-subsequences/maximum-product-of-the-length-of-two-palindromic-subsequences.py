import heapq
class Solution:
    def maxProduct(self, s: str) -> int:

        ans = 0

        store = {}

        def function_to_create_word(mask):
            word = ''

            for i in  range(len(s)):
                if (1 << i) & mask:
                    word += s[i]

            return word
        
        for i in range(1, 1<<len(s)):
            subseq = function_to_create_word(i)
            if subseq == subseq[::-1]:
                store[i] = len(subseq)

        for key, val in store.items():
            for key2, val2 in store.items():
                if not key & key2:
                    if store[key] * store[key2] > ans:
                        ans = store[key] * store[key2]

        return ans
        
        