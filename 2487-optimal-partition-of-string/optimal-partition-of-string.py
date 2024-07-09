class Solution:
    def partitionString(self, s: str) -> int:
        
        store = set()
        count = 0
        for letter in s:
            if letter not in store:
                store.add(letter)
            else:
                store = set()
                store.add(letter)
                count += 1

        return count + 1