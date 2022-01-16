from util.StatusEnum import StatusEnum


class Order():
    def __init__(self):
        self.__order_id = None
        self.__meals = []
        self.__distance = float(0)
        self.__status = StatusEnum.INITIATED.name
        self.__orderTime = float(0)

    def setOrderTime(self, time):
        self.__orderTime = float(time)

    def getOrderTime(self):
        return self.__orderTime

    def setOrderId(self, id):
        self.__order_id = id

    def getOrderId(self):
        return self.__order_id

    def setMeals(self, meals):
        self.__meals = meals

    def getMeals(self):
        return self.__meals

    def setDistance(self, distance):
        self.__distance = distance

    def getDistance(self):
        return self.__distance

    def setStatus(self, status):
        self.__status = status

    def getStatus(self):
        return self.__status
