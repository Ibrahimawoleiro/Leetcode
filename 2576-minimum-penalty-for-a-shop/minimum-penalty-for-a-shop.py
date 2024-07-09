class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        left = [0 for num in range(len(customers) + 1)]
        right = [0 for num in range(len(customers) + 1)]

        n_count = 0
        y_count = 0
        for index in range(len(customers) + 1):
            if index == 0:
                if customers[index] == 'N':
                    n_count += 1
                continue
            left[index] = n_count
            if index < len(customers) and customers[index] == 'N':
                n_count += 1 

        for index in range(len(customers), -1 ,-1):
            if index == len(customers):
                continue
            if customers[index] == 'Y':
                y_count += 1
            right[index] = y_count

        ans = [float('inf'), float('inf')]
        for index in range(len(customers) + 1):
            curr = left[index] + right[index]
            if curr < ans[0]:
                ans[0] = curr
                ans[1] = index
        return ans[1]