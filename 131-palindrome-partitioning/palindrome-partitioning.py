class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ans = []
        curr = []

        def isPalindrome(start, end):
            while(start <= end):
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def helper(current, start):
            if start == len(s):
                ans.append(current.copy())
                return

            for index in range(start,len(s)):
                print(current,"start index ->",start)
                if isPalindrome(start,index):
                    current.append(s[start:index+1])
                    helper(current,index + 1)
                    current.pop()
      
        helper([],0)

        return ans
                


                

        



        

