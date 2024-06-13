class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        store = set()
        for arr in paths:
            store.add(arr[1])
        for arr in paths:
            if arr[0] in store:
                store.remove(arr[0])
        return store.pop()