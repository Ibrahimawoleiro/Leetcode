# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        root_position = (0,0)
        column_dictionary = {}
        column_rank  = []
        rank_values = {}
        ans = []
        self.helper(root, column_dictionary, column_rank, root_position, rank_values)

        while(column_rank):
            column_result = []
            c = heapq.heappop(column_rank)
            while(column_dictionary[c]):
                r = heapq.heappop(column_dictionary[c])
                while rank_values[(r,c)]:
                    column_result.append(heapq.heappop(rank_values[(r,c)]))
            ans.append(column_result)
        return ans
    #root -> current node
    #r_p -> root position
    #c_rk -> the columns rank for when you start getting the values
    #c_d -> dictionary that models the relationship columns -> rows heap
    #r_v -> dictionary that models (c,r) -> values and if (c,r) is already present,append to it.
    #Note: the values for (c,r) are also a heap to get the values in sorted order
    def helper(self, root, c_d, c_rk, r_p, r_v):
        if not root:
            return 

        self.helper(root.left, c_d, c_rk, (r_p[0] + 1, r_p[1] - 1), r_v)

        self.helper(root.right, c_d, c_rk, (r_p[0] + 1, r_p[1] + 1), r_v)

        c = r_p[1]
        r = r_p[0]
        #If the column isn't present in c_d
        if c not in c_d:
            #Add the column to heap and the column_dictionary which points to heap of rows
            heappush(c_rk, c)
            #Now we have a heap at the column
            c_d[c] = []
            #Now we add the row, but we have to check in r_v if that combination exist
            heapq.heappush(c_d[c], r)

            r_v[(r,c)] = []

            heapq.heappush(r_v[(r,c)], root.val)

        else:
            #If the combination is already present in r_v
            if (r, c) in r_v:
                heapq.heappush(r_v[(r,c)], root.val)
            #If the combination isn't present
            else:
                heapq.heappush(c_d[c], r)
                r_v[(r,c)] = []
                heapq.heappush(r_v[(r,c)], root.val)






