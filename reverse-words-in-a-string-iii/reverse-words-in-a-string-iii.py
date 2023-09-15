class Solution:
    def reverseWords(self, s: str) -> str:
        holder = s.split(" ")
        
        result = ["".join(reversed(word)) for word in holder]
        
        return " ".join(result)