class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #Every partition is a beginning 
        #And every partition should move from size 1 to the end of the array
        #Every partition should not move to the next size unless the current size is a palindrome
        ans = []
        def helper(b,curr):
            print(b,len(s),curr)
            if b>= len(s):
                ans.append(curr.copy())
                return
            #End of current partition and beginning of next partition
            for index in range(b+1, len(s) + 1):
                c = s[b:index]
                #Check if the word is a palindrome
                i = 0
                j = len(c) - 1
                palindrome = False
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