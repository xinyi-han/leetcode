class SmallestInfiniteSet:

    def __init__(self):
        self.hashSet = {i for i in range(1, 1001)}

    def popSmallest(self) -> int:
        num = min(self.hashSet)
        self.hashSet.remove(num)
        return num

    def addBack(self, num: int) -> None:
        self.hashSet.add(num)
