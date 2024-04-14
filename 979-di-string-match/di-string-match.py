class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = []
        store = set()
        i = len(s)
        j = 0
        for val in range(len(s)+1):
            store.add(val)

        for char in s:
            if char == 'I':
                ans.append(j)
                store.remove(j)
                j+=1
            else: 
                ans.append(i)
                store.remove(i)
                i-=1
                
        ans.append(store.pop())
        return ans
        