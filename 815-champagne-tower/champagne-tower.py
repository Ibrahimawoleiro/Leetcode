class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0

        #Store stores the remainder after removing val for row i, col j
        store = {}
        #fill store how filled each row i at index j is 
        fill = {}

        for r in range(query_row + 1):
            for c in range(r + 1):
                if r == 0:
                    if poured > 0:
                        if poured >= 1:
                            fill[(0,0)] = 1
                            store[(0,0)] = poured - 1
                        else:
                            fill[(0,0)] = poured
                            store[(0,0)] = 0
                    else:
                        store[(0,0)] = 0
                        fill[(0,0)] = 0
                else:
                    left = store[(r - 1, c - 1)] / 2 if (r-1,c-1) in store  else 0
                    right = store[(r - 1, c )] / 2 if (r-1,c) in store else 0
                    curr = left + right
                    if curr > 0:
                        if curr >= 1:
                            fill[(r,c)] = 1
                            store[(r,c)] = curr - 1
                        else:
                            fill[(r,c)] = curr
                            store[(r,c)] = 0
                    else:
                        store[(r,c)] = 0
                        fill[(r,c)] = 0
        print(fill)
        print(store)
        return fill[(query_row, query_glass)]