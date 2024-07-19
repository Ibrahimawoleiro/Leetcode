class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''
        left = 0
        right = len(self.store[key]) - 1
        curr = self.store[key]
        while left <= right:
            mid = (left + right) // 2
            
            if curr[mid][0] == timestamp:
                return curr[mid][1]
            elif curr[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        # if left < len(curr) and right >= 0:
        #     if curr[left][0] < curr[right][0]:
        #         return curr[left][1]
            
        #     return curr[right][1]
        
        # if left < len(curr):
        #     if curr[left][0] < timestamp:
        #         return curr[left][1]
        
        if right >= 0 and curr[right][0] < timestamp:
            return curr[right][1]

        return ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)