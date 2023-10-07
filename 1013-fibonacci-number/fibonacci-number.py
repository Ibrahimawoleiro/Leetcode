class Solution:

    def fib(self, n: int) -> int:

        if(n==0):
            return 0
        
        if(n==1):
            return 1
        
        
        dictionary = {
            0:0,
            1:1
        }

        left = self.helper(dictionary,n-1)

        right = self.helper(dictionary,n-2)

        return left + right

    def helper(self,dictionary, n):
        if n in dictionary:
            return dictionary[n]

        left = self.helper(dictionary,n-1)

        right = self.helper(dictionary,n-2)

        dictionary[n]=left+right

        return left + right

        