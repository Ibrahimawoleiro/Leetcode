class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        seen = set()
        self.helper(s,0,seen)
        return list(seen)

    def helper(self,curr,index,seen):
        if index >= len(curr):
            return 
        print(curr, index, curr)
        seen.add(curr)

        if curr[index].isalpha() and curr[index].isupper() :

            temp = list(curr)
            temp[index] = temp[index].lower()
            if "".join(temp) not in seen:

                self.helper("".join(temp), index, seen) 

        elif curr[index].isalpha() and curr[index].islower():
            temp = list(curr)
            temp[index] = temp[index].upper()
            if "".join(temp) not in seen:
                self.helper("".join(temp), index, seen) 
        
        self.helper(curr, index+1, seen) 
