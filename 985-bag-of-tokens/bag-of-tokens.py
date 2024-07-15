class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i = 0
        j = len(tokens) - 1
        m = 0
        curr = 0
        while i <= j:
            if power >= tokens[i]:
                curr += 1
                power -= tokens[i]
                if curr > m:
                    m = curr
                i += 1
            else:
                if curr > 0:
                    power += tokens[j]
                    j -= 1
                    curr -= 1

                else:
                    break

        return m
