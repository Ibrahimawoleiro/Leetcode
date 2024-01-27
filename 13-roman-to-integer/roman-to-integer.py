class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        total = 0
        pointer = len(s) - 1
        while(pointer >= 0):
            if pointer == len(s) - 1:
                total += dictionary[s[pointer]]
                pointer -= 1
                continue
            if dictionary[s[pointer + 1]] <= dictionary[s[pointer]]:
                total += dictionary[s[pointer]]
            else:
                total -= dictionary[s[pointer]]
            pointer -= 1
        return total
        
        