class Solution:
    def isPalindrome(self, x: int) -> bool:
        checker = str(x)
        right = len(checker)-1
        left = 0

        while left <= right:
            if checker[left] != checker[right]:
                return False
            left+=1
            right-=1

        return True