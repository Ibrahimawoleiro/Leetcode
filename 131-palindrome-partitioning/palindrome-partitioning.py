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
            #Check subarrays starting from beginning to end of arr
            #End of current partition and beginning of next partition
            for index in range(b+1, len(s) + 1):
                #Create a subword
                
                #Put a pointer at the beginning of subword and end of subword
                i = b
                j = index - 1
                palindrome = False
                #Check if the word is a palindrome
                while i <= j:
                    if s[i] != s[j]:
                        break
                    i+=1
                    j-=1
                    if i > j:
                        palindrome = True
                #If it is a palindrome, append it to current
                #Then check different combination for the right side
                if palindrome:
                    curr.append(s[b:index])
                    helper(index, curr)
                    curr.pop()
        helper(0,[])
        return ans