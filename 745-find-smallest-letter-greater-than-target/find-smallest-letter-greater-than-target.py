class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # #Approach 1
        # first_greater = letters[0]

        # for letter in letters:
        #     if letter > target:
        #         return letter
        # return first_greater

        #Approach 2

        left = 0
        right = len(letters) - 1
        first_greater = 0
        while(left<=right):
            
            mid = int((left + right) / 2)

            if letters[mid] <= target:
                left = mid + 1
            
            else:
                if mid - 1 >= 0 and letters[mid - 1] > target:
                    right = mid - 1
                else:
                    return letters[mid]

        return letters[0] 