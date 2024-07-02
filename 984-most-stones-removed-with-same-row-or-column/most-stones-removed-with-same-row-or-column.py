class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row_len = 0
        col_len = 0
        store = set()
        for location in stones:
            row_len = max(row_len, location[0])
            col_len = max(col_len, location[1])

        row_len += 1
        col_len += 1

        print(row_len, col_len)

        parent = [num for num in range(row_len + col_len)]
        size = [1 for num in range(row_len + col_len)]

        def find_ul_parent(curr):
            u_p = parent[parent[curr]]
            c_p = parent[curr]
            while c_p != u_p:
                c_p = u_p
                u_p = parent[u_p]
            parent[curr] = u_p

            return u_p

        for location in stones:

            column = (row_len  - 1 ) + location[1] + 1
            row = location[0]

            store.add(row)
            store.add(column)


            column_ul = find_ul_parent(column)
            row_ul = find_ul_parent(row)

            if size[row_ul] == size[column_ul]:
                size[row_ul] += size[column_ul]
                parent[column_ul] = row_ul
            else:
                if size[row_ul] > size[column_ul]:
                    size[row_ul] += size[column_ul]
                    parent[column_ul] = row_ul
                else:
                    size[column_ul] += size[row_ul]
                    parent[row_ul] = column_ul
        
        count = 0
        for num in store:
            if num == find_ul_parent(num):
                count += 1

        return len(stones) - count