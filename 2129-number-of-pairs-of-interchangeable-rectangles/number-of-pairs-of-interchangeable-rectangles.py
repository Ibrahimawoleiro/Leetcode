class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        store = {}
        ans = 0
        for r in rectangles:
            curr = r[0]/r[1]
            if curr not in store:
                store[curr] = 1
            else:
                store[curr] += 1

        for v in store.values():
            if v > 1:
                ans += (v * (v-1))/2

        return int(ans)
