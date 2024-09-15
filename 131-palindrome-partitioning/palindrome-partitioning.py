class Solution:
    def partition(self, word: str) -> List[List[str]]:
        def palindrome(left, right):
            while left <= right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True
        ans = []
        def rec(s, e,combo):
            if s >= len(word):
                ans.append(combo.copy())
                return
            for end in range(e, len(word)):
                if palindrome(s,end):
                    combo.append(word[s:end + 1])
                    rec(end + 1, end + 1,combo)
                    combo.pop()
        rec(0,0,[])
        return ans
