class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        #The parent array represents the ultimate parent for each index
        parent = [num for num in range(len(grid) * len(grid[0]))]

        #The size array represents number of emails that are connected to the the current index
        size = [1 for num in range(len(grid) * len(grid[0]))]

        #Function to get the ultimate parent
        def find_ultimate_parent(node):
            if node == parent[node]:
                return node

            ultimate_parent =  find_ultimate_parent(parent[node])

            parent[node] = ultimate_parent

            return ultimate_parent

        def merge(prev_ul,curr_ul):
            if size[prev_ul] >= size[curr_ul]:
                size[prev_ul] += size[curr_ul]
                parent[curr_ul] = prev_ul
            else:
                size[curr_ul] += size[prev_ul]
                parent[prev_ul] = curr_ul
        number = -1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                number += 1
                if grid[r][c] == 1:

                    #Merge the top and left neighbor if they are 1
                    top_n = number - len(grid[0])
                    left_n = number - 1

                    #check for top neighbor
                    if r - 1 >= 0 and grid[r - 1][c] == 1:
                        top_ul = find_ultimate_parent(top_n)
                        curr_ul = find_ultimate_parent(number)
                        
                        if top_ul != curr_ul:
                            merge(top_ul, curr_ul)
                    #check for left neighbor
                    if c - 1 >= 0 and grid[r][c - 1] == 1:
                        left_ul = find_ultimate_parent(left_n)
                        curr_ul = find_ultimate_parent(number)
                        
                        if left_ul != curr_ul:
                            merge(left_ul, curr_ul)

        ans = max(size)

        for num in range(len(grid) * len(grid[0])):
            parent[num] = find_ultimate_parent(num)

        number = -1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                number += 1
                if grid[r][c] == 0:
                    curr_total = 0
                    seen = set()
                    if r - 1 >= 0 and grid[r - 1][c] == 1:
                        n_ul = find_ultimate_parent(number - len(grid[0]))
                        curr_total += size[find_ultimate_parent(number - len(grid[0]))]
                        seen.add(n_ul)
                    if r + 1 < len(grid) and grid[r + 1][c] == 1:
                        n_ul = find_ultimate_parent(number + len(grid[0]))
                        if n_ul not in seen:
                            curr_total += size[find_ultimate_parent(number + len(grid[0]))]
                            seen.add(n_ul)
                    if c - 1 >= 0 and grid[r][c - 1] == 1:
                        n_ul = find_ultimate_parent(number - 1)
                        if n_ul not in seen:
                            curr_total += size[find_ultimate_parent(number - 1)]
                            seen.add(n_ul)
                    if c + 1 < len(grid[0]) and grid[r][c+1] == 1:
                        n_ul = find_ultimate_parent(number + 1)
                        if n_ul not in seen:
                            curr_total += size[find_ultimate_parent(number + 1)]
                            seen.add(n_ul)
                    ans = max(ans, curr_total + 1)

        
        print(parent)
        print(size)
        return ans

        
            
        