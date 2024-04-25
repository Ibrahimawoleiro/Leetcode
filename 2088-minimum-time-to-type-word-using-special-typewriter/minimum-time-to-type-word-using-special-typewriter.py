class Solution:
    def minTimeToType(self, word: str) -> int:
        count = 0
        prev = 'a'
        for val in word:
            if val == prev:
                count+=1
                continue
            clockwise = abs(ord(prev)- ord(val))
            print(clockwise)
            count += min(clockwise, 26 - clockwise) + 1
            prev = val
        return count