from abc import ABCMeta, abstractmethod


class KitchenService(metaclass=ABCMeta):
    @abstractmethod
    def addOrders(self, order, time, slot):
        pass

    @abstractmethod
    def getSlotStatus(self):
        pass

    @abstractmethod
    def getCurrentOrders(self):
        pass

    @abstractmethod
    def getCurrentOrderById(self, id):
        pass

    @abstractmethod
    def setSlotStatus(self, slot):
        pass