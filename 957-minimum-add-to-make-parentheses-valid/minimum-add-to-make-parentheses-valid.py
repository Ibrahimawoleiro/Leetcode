class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        checker = []

        for input in s:
            if input == "(":
                checker.append(input)
            elif input == ")" and checker and checker[len(checker)-1] == "(":
                checker.pop()

            else:
                checker.append(input)

        
        return len(checker)