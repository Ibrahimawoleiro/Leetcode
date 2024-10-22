class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1 for _ in range(len(s))]
        def rec(i):
            if i >= n:
                return True
            if dp[i] != -1:
                return True if dp[i] == 1 else 0
            for word in wordDict:
                if i + len(word) <= n:
                    if s[i: i + len(word)] == word:
                        if rec(i + len(word)):
                            dp[i] = 1
                            return True
            dp[i] = 0
            return False
        return rec(0)