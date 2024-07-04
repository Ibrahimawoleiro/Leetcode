class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        for curr in strs:
            if len(curr) < len(word):
                word = curr
        for index in range(len(strs)):
            for l_i in range(len(strs[index])):
                if l_i >= len(word) or word[l_i] != strs[index][l_i]:
                    word = word[0:l_i]
                    break

        return word      