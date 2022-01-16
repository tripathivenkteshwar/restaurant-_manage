from abc import ABCMeta,abstractmethod


class OrderService(metaclass = ABCMeta):
    @abstractmethod
    def addOrders(self, id, meals, distance):
        pass

    @abstractmethod
    def getOrders(self):
        pass

    @abstractmethod
    def getOrdersById(self, id):
        pass