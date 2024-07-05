class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        store = {}

        for letter in text:
            if letter in store:
                store[letter] += 1
            else:
                store[letter] = 1
        
        m = float('inf')

        if 'l' not in store or 'o' not in store:
            return 0
        store['l'] = floor(store['l'] / 2 )
        store['o'] = floor(store['o'] / 2 )

        for letter in 'balloon':
            if letter not in store:
                return 0
            if store[letter] < m:
                m = store[letter]

        return m