class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #Approach1
        for val in range(len(letters)):
            if letters[val] > target:
                return letters[val]
        
        return letters[0]