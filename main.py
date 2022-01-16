from service.KitchenServiceImpl import KitchenServiceImpl
from service.OrderServceImpl import OrderServiceImpl
from controller.KitchenController import KitchenController
from controller.OrderController import OrderController
from util.StatusEnum import StatusEnum

def driver():
    
    input_val = [{"orderId": 12, "meals": ["A", "A"], "distance": 1},
             {"orderId": 21, "meals": ["A", "A","A"], "distance": 1},
                 {"orderId": 26, "meals": ["M", "M","A"], "distance": 1},
             {"orderId": 14, "meals": ["M", "M", "M", "M", "A", "A", "A"], "distance": 10},
             {"orderId": 32, "meals": ["M", "A"], "distance": 0.1},
             {"orderId": 22, "meals": ["A"], "distance": 3}]

    kitchen_controller = KitchenController(KitchenServiceImpl())
    order_controller = OrderController(OrderServiceImpl())

    for order_data in input_val:
        order_controller.addOrders(order_data["orderId"], order_data["meals"], order_data["distance"])

    orders = order_controller.lookupAllOrders()

    for id, order_details in orders.items():
        slot_availble = kitchen_controller.getSlotStatus()
        status = kitchen_controller.addOrders(order_details, slot_availble)
        #print(status)
    allOrers =order_controller.lookupAllOrders()
    for data in input_val:
        singleOrder=allOrers.get(data.get("orderId"))
        if singleOrder.getStatus() == StatusEnum.FAIL.name or singleOrder.getStatus() == StatusEnum.DENIED.name:
            print("Order ", singleOrder.getOrderId(), " is denied because the restaurant cannot accommodate it.")
        else:
            order_time = int(singleOrder.getOrderTime()) if (singleOrder.getOrderTime() - int(singleOrder.getOrderTime()) == 0) \
                else float(singleOrder.getOrderTime())
            print("Order ", singleOrder.getOrderId(), " will get delivered in", order_time)



if __name__ == '__main__':
    driver()
