class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        storeA = {}
        storeB = {}

        for i in range(len(t)):

            if s[i] in storeA and storeA[s[i]] != t[i]:
                return False
            
            if t[i] in storeB and storeB[t[i]] != s[i]:
                return False

            storeA[s[i]] = t[i]
            storeB[t[i]] = s[i]

        return True