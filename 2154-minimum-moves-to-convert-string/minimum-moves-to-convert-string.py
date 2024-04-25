class Solution:
    def minimumMoves(self, s: str) -> int:
        i = 0
        operations = 0
        x_seen = 0

        while(i < len(s)):
            if s[i] != 'X':
                i+=1
                continue
            count = 3
            while(count > 0 and i < len(s)):
                if s[i] == 'X':
                    x_seen +=1
                count -= 1
                i+=1
            if x_seen > 0:
                operations += 1
                x_seen = 0

        return operations
