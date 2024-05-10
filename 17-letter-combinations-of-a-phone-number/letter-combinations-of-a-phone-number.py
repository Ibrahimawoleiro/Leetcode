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

        #Make a recursive function to loop through every value at index for diff combination
        ans = []
        def recursive(index,curr):
            if index >= len(digits):
                if len(curr) > 0:
                    ans.append(curr)
                return 
            for val in dictionary[digits[index]]:
                #Add one of the val matched to digits[i] to curr
                curr = curr + val
                recursive(index + 1, curr)
                curr = curr[:-1]

        recursive(0, '')
        return ans