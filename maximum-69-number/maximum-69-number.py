class Solution:
    def maximum69Number (self, num: int) -> int:
        num_to_string = str(num)
        
        for digit in range(len(num_to_string)):
            print(num_to_string[digit], "g")
            if num_to_string[digit] == "6":
                k=num_to_string.replace("6","9",1)
                print(k)
                ans = int(k)
                return ans
            
        return num