class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        l = list(string.ascii_lowercase)
        
        storeA = {}
        storeB = {}
        seen = set()
        count = 0
        for i in range(len(s)):
            if i == 0:
                storeA[s[i]] = 1
            else:
                if s[i] not in storeB:
                    storeB[s[i]] = 1
                else:
                    storeB[s[i]] += 1

        
        for i in range(1, len(s)):
            current = s[i]
            if current in storeB:
                storeB[current] -= 1
                if storeB[current] == 0:
                    del storeB[current]

            for j in range(len(l)):
                curr = (l[j], current, l[j])
                if l[j] in storeA and l[j] in storeB:
                    if curr not in seen:
                        seen.add(curr)
                        count += 1
                    

            
            if current in storeA:
                storeA[current] += 1
            else:
                storeA[current] = 1
            
                
        return count