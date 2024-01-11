class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #Approach 1
        first_greater = letters[0]

        for letter in letters:
            if letter > target:
                return letter
        return first_greater
