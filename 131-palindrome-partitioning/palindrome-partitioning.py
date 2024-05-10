class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #Every partition is a beginning 
        #And every partition should move from size 1 to the end of the array
        #Every partition should not move to the next size unless the current size is a palindrome
        ans = []
        def helper(b,curr):
            if b>= len(s):
                ans.append(curr.copy())
                return
            #End of current partition and beginning of next partition
            for index in range(b+1, len(s) + 1):
                #Create a subword
                c = s[b:index]
                #Put a pointer at the beginning of subword and end of subword
                i = 0
                j = len(c) - 1
                palindrome = False
                #Check if the word is a palindrome
                while i <= j:
                    if c[i] != c[j]:
                        break
                    i+=1
                    j-=1
                    if i > j:
                        palindrome = True
                if palindrome:
                    curr.append(c)
                    helper(index, curr)
                    curr.pop()
        helper(0,[])
        return ans