class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        start = {}
        end = {}
        for i in range(len(s)):
            if s[i] not in start:
                start[s[i]] = i

        for i in range(len(s)):
            end[s[i]] = i
        ans = -1
        for (key, val) in end.items():
            if end[key] != start[key]:
                if end[key] - start[key] - 1 > ans:
                    ans = end[key] - start[key] - 1
        return ans
