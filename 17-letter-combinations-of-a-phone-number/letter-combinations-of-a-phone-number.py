class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans = []
        def rec(store, index, combo):
            if index == len(digits):
                if len(combo) > 0:
                    ans.append(combo)
                return
            #Recursive Case
            for val in store[digits[index]]:
                rec(store, index + 1, combo + val)
        rec(dictionary, 0, '')
        return ans