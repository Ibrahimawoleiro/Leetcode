import queue
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        q = queue.Queue()
        
        d = float('inf')
        #(row, column, distance)
        q.put((0,0,1))
        done = set()
        done.add((0,0))
        while not q.empty():
            row, col, d = q.get()
            if (row,col) == (len(grid) - 1 , len(grid[0]) - 1) and grid[len(grid) - 1][len(grid[0]) - 1] == 0:
                return d
            if grid[row][col] == 1:
                continue
            
            if row > 0:
                if (row - 1, col) not in done:
                    q.put((row - 1, col, d + 1))
                    done.add((row - 1, col))
            if row < len(grid) - 1:
                if (row + 1, col) not in done:
                    q.put((row + 1, col, d + 1))
                    done.add((row + 1, col))
            if col > 0:
                if (row , col - 1) not in done:
                    q.put((row , col - 1, d + 1))
                    done.add((row, col - 1))
            if col < len(grid[0]) - 1:
                if (row, col + 1) not in done:
                    q.put((row, col + 1, d + 1))
                    done.add((row, col + 1))
            # Check top-left diagonal
            if row > 0 and col > 0:
                if (row - 1, col - 1) not in done:
                    q.put((row - 1, col - 1, d + 1)) 
                    done.add((row - 1, col - 1))
            # Check bottom-left diagonal
            if row < len(grid) - 1 and col > 0:
                if (row + 1, col - 1) not in done:
                    q.put((row + 1, col - 1, d + 1)) 
                    done.add((row + 1, col - 1))
            # Check top-right diagonal
            if row > 0 and col < len(grid[0]) - 1:
                if (row - 1, col + 1) not in done:
                    q.put((row - 1, col + 1, d + 1)) 
                    done.add((row - 1, col + 1))
            # Check bottom-right diagonal
            if row < len(grid) - 1 and col < len(grid[0]) - 1:
                if (row + 1, col + 1) not in done:
                    q.put((row + 1, col + 1, d + 1)) 
                    done.add((row + 1, col + 1))
        
        return -1