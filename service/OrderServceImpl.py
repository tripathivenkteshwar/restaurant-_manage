from service.OrderService import OrderService
from models.Order import Order
from collections import OrderedDict


class OrderServiceImpl(OrderService):

    orderList = OrderedDict()

    def addOrders(self, id, meals, distance):
        order_details = Order()
        order_details.setOrderId(id)
        order_details.setMeals(meals)
        order_details.setDistance(distance)
        self.__class__.orderList[id] = order_details

    def getOrders(self):
        return self.__class__.orderList

    def getOrdersById(self, id):
        return self.__class__.orderList.get(id)