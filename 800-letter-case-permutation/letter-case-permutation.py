class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        seen = set()
        def helper(word,index):
            if index > len(s) - 1:
                return
            curr = word.copy()
            if word[index].isalpha():
                print(word[index])
                lower = curr[index].lower()
                up = curr[index].upper()
                curr[index] = lower
                seen.add("".join(curr))
                helper(list(curr), index + 1)
                curr[index] = up
                seen.add("".join(curr))
                helper(list(curr), index + 1)
            else:
                helper(word, index + 1)
        helper(list(s),0)

        return list(seen) if seen else  [s]