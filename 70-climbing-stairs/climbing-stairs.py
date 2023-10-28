class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 1

        ways = 0

        dictionary={
            n:1,
            n-1:1
        }
     
        return  self.helper(dictionary,0,ways,n,n-1)
     
    def helper(self, dictionary,beginning,ways,max,second_max):
        if beginning == max or beginning == second_max:
            return 1
        elif beginning in dictionary:
            return dictionary[beginning]
        if(beginning+1 <= max):
            ways += self.helper(dictionary,beginning+1,ways,max,second_max)
        
        if(beginning + 2 <= max):
            ways += self.helper(dictionary,beginning+2,ways,max,second_max)

        if beginning not in dictionary:
            dictionary[beginning]= ways
        return ways