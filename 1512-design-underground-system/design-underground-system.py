class UndergroundSystem:

    def __init__(self):
        self.trips = {}
        self.checked_in = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_info = self.checked_in[id]
        journey = (start_info[0],stationName)

        if journey not in self.trips:
            self.trips[journey] = [t - start_info[1]]
        else:
            self.trips[journey].append(t-start_info[1])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        count = 0

        total = 0

        curr = self.trips[(startStation, endStation)]

        for num in curr:
            total += num
            count += 1

        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)