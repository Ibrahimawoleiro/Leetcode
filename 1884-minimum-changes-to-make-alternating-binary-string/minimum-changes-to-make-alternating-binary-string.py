class Solution:
    def minOperations(self, s: str) -> int:
        count_z = 0
        count_o = 0

        last = '0'
        for i in range(len(s)):
            if s[i] != last:
                count_z += 1
            
            last = '0' if last == '1' else '1'

        last = '1'
        for i in range(len(s)):
            if s[i] != last:
                count_o += 1
            
            last = '0' if last == '1' else '1'
        print(count_z)
        print(count_o)
        return min(count_o, count_z)