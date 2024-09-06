class Solution:
    def isPalindrome(self, x: int) -> bool:
        def rev(num):
            result = 0
            dummy = num

            while dummy > 0:
                digit = dummy % 10
                result = (result * 10) + digit
                dummy = dummy // 10

            if result > 2 ** 31:
                return 0

            return result if num > 0 else -result

        return x == rev(x)