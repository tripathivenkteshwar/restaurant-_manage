class Kitchen:
    def __init__(self, order, kitchen_time, slot):
        self.__slot = slot
        self.__order = order
        self.kitchen_time = kitchen_time

    def getSlot(self):
        return self.__slot

    def setSlot(self, slot):
        self.__slot = slot

    def getOrder(self):
        return self.__order

    def setOrder(self, order):
        self.__order = order

    def getKitchenTime(self):
        return self.kitchen_time

    def setKitchenTime(self, time):
        self.kitchen_time = time

    def __lt__(self, other):
        return self.kitchen_time < other.kitchen_time