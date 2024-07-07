class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        checker = {}
        ans = []
        for letter in p:
            if letter in checker:
                checker[letter] += 1
            else:
                checker[letter] = 1
        
        store = {}
        for index in range(len(p)):
            if s[index] in store:
                store[s[index]] += 1

            else:
                store[s[index]] = 1
        if store == checker:
            ans.append(0)

        i = 0
        j = len(p)

        while j < len(s):
            store[s[i]] -= 1
            if store[s[i]] == 0:
                del store[s[i]]
            i += 1
            if s[j] in store:
                store[s[j]] += 1
            else:
                store[s[j]] = 1
            j += 1

            if store == checker:
                ans.append(i)

        return ans