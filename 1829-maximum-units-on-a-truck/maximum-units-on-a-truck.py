import heapq
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        rank = []
        heapq.heapify(rank)
        store_A = {}
        store_B = {}
        total = 0
        for arr_index in range(len(boxTypes)):
            if -1 * boxTypes[arr_index][1] not in store_A:
                store_A[-1 * boxTypes[arr_index][1]] = [arr_index]
                store_B[arr_index] = boxTypes[arr_index][0]
            else:
                print(store_A[-1 * boxTypes[arr_index][1]], 'jhgfghj')
                store_A[-1 * boxTypes[arr_index][1]].append(arr_index)
                store_B[arr_index] = boxTypes[arr_index][0]
        
        for number in store_A.keys():
            heapq.heappush(rank,number)

        while(truckSize > 0 and len(rank) > 0):
            curr = -1 * heapq.heappop(rank)
            for val in store_A[-1 * curr]:
                while(store_B[val] > 0):
                    store_B[val] -= 1
                    truckSize -= 1
                    total += curr
                    if truckSize == 0:
                        break
                if truckSize == 0:
                    break

        return total
        
