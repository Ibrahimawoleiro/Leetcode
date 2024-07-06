class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        store = {}

        for word in strs:
            curr = tuple(sorted(word))
            if curr in store:
                store[curr].append(word)
            else:
                store[curr] = [word]
        
        ans = []

        for arr in store.values():
            ans.append(arr)

        return ans