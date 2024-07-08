class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 11:
            return []
        checker = s[0:10]
        i = 0
        j = 10
        store = set()
        ans = set()
        while j <= len(s):
            if checker not in store:
                store.add(checker)
            else:
                ans.add(checker)
            i += 1
            j += 1
            checker = s[i: j]
        
        return list(ans)