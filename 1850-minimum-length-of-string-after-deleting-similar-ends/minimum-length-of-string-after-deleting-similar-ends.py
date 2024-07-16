class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        left_boundary = -1
        right = len(s) - 1
        right_boundary = len(s)


        while left < right:
            if s[left] != s[right]:
                break
            
            left_store = s[left]
            while left - 1 <= left_boundary or left < len(s) and s[left] == left_store:
                left+= 1

            left_boundary = left - 1

            right_store = s[right]

            while right + 1 >= right_boundary or right > 0 and s[right] == right_store:
                right -= 1

            right_boundary = right + 1

 
        curr = (right - left) + 1
        return curr   if curr > 0 else 0