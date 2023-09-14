class Solution:
    def maximum69Number (self, num: int) -> int:
        num_to_string = str(num)
        
        for digit in range(len(num_to_string)):
            if num_to_string[digit] == "6":
                k=num_to_string.replace("6","9",1)
                ans = int(k)
                return ans
            
        return num