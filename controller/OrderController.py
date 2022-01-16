class OrderController:
    def __init__(self, orderService):
        self.order_service = orderService

    def addOrders(self, id, meals, distance):
        self.order_service.addOrders(id, meals, distance)

    def updateOrderStatus(self, id, status):
        order_details = self.order_service.getOrdersById(id)
        order_details.setStatus(status)

    def lookupAllOrders(self):
        return self.order_service.getOrders()
