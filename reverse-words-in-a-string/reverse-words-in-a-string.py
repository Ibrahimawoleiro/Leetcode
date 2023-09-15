class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Strip the string 
        
        Split the word by  " " and put in a variable holder
        
        Strip every word in holder
        
        Then join each index by " "
        
        Then return
        
        """
        
        stripped = s.strip()
        
        holder = stripped.split(" ")
        
        real_holder = [curr for curr in holder if curr != ""]
        
        print(real_holder)
        
        real_holder.reverse()
        
        return " ".join(real_holder)