class UndergroundSystem:

    def __init__(self):
        self.idList = collections.defaultdict(list)
        self.stationTime = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.idList[id].append([stationName, t])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        obj = self.idList[id][0]
        self.stationTime[(obj[0], stationName)].append(t-obj[1])
        self.idList.pop(id)

    def getAverageTime(self, start: str, end: str) -> float:
        station = (start, end)
        times = self.stationTime[station]
        return sum(times) / len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)