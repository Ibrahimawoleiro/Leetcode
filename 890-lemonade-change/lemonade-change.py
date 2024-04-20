class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        store = {5:0, 10:0, 20:0}

        for val in bills:
            if val == 5:
                store[val] += 1
            elif val == 10:
                if store[5] <= 0:
                    return False
                store[5] -= 1
                store[val]+= 1
            else:
                if store[10] > 0 and store[5] > 0:
                    store[10] -=1
                    store[5] -= 1
                    store[20]+=1
                elif store[5] >= 3:
                    store[5] -=3
                else:
                    return False
            
        return True
