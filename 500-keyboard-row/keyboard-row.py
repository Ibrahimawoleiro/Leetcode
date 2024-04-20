class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []

        checker = [set("qwertyuiopQWERTYUIOP"),set("asdfghjklASDFGHJKL"),set("zxcvbnmZXCVBNM")]

        for word in words:
            for check in checker:
                char_index = 0
                while char_index < len(word):
                    if word[char_index] not in check:
                        print(word[char_index])
                        break
                    char_index+=1
                
                if char_index == len(word):
                    ans.append(word)
                    break
        return ans
                