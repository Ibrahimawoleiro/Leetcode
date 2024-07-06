class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        heap = []
        store = {}
        for r_i in range(len(wall)):
            total = 0
            for c_i in range(len(wall[r_i]) -  1):
                total += wall[r_i][c_i]
                if total not in store:
                    store[total] = 1
                else:
                    store[total] += 1
        top = 0
        print(top, store)
        for val in store.values():
            if val > top:
                top = val

        return len(wall) - top