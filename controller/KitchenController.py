from util.StatusEnum import StatusEnum
from util.MealsEnum import MealsEnum
import heapq as hq

MAX_SLOT = 7
MAX_TIME = 150.0
TIME_PER_KM_DISTANCE = 8.0


class KitchenController:
    def __init__(self, kitchenService):
        self.kitchen_service = kitchenService

    def addOrders(self, order, slotAvailable):
        time = 0
        slot = 0

        for mealtype in order.getMeals():
            if mealtype == MealsEnum.A.name:
                time = max(time,float(MealsEnum.A.value.get("minutes")))
                slot = slot + int(MealsEnum.A.value.get("cooking_slots"))

            if mealtype == MealsEnum.M.name:
                time = max(time, float(MealsEnum.M.value.get("minutes")))
                slot = slot + int(MealsEnum.M.value.get("cooking_slots"))

        # 14 point
        if slot > MAX_SLOT:
            order.setStatus(StatusEnum.FAIL.name)
            return StatusEnum.FAIL.name

        # 150 min
        if time+self.kitchen_service.getKitchenTimeWait()+ self.distanceTimeCalc(order)> MAX_TIME:
            order.setStatus(StatusEnum.DENIED.name)
            return StatusEnum.DENIED.name

        #order process

        if slot <= slotAvailable:
            order.setStatus(StatusEnum.PROCESS.name)
            self.kitchen_service.addOrders(order, time+self.distanceTimeCalc(order), slot)
            return StatusEnum.PROCESS.name

        elif slot > slotAvailable:
            order.setStatus(StatusEnum.WAIT.name)

            while True:

                if slotAvailable < 7 and slot - slotAvailable >0:

                    val = self.getSlotForOrders()

                    if val == "not":
                        break
                    self.kitchen_service.setSlotStatus(val)
                    slotAvailable = self.kitchen_service.getSlotStatus()
                else:
                    break

            order.setStatus(StatusEnum.PROCESS.name)

            self.kitchen_service.addOrders(order, time+self.distanceTimeCalc(order), slot)
            return StatusEnum.PROCESS.name

    def getSlotForOrders(self):
        current_orders = self.kitchen_service.getCurrentOrders()
        if len(current_orders)==0:
            return "not"
        hq.heapify(current_orders)
        order = current_orders.pop(0)
        free_slot = order.getSlot()
        #print("slot",free_slot, order.getOrder().getOrderId())

        order.getOrder().setStatus(StatusEnum.COMPLETED.name)
        final_time = order.getOrder().getOrderTime()

        self.kitchen_service.updateKitchenTimeWait(float(final_time))


        hq.heapify(current_orders)
        while current_orders:
            new_time = current_orders[0].getOrder().getOrderTime()
            if new_time == final_time:
                hq.heapify(current_orders)
                order_val = current_orders.pop(0)
                order_val.getOrder().setStatus(StatusEnum.COMPLETED.name)
                free_slot = free_slot + order_val.getSlot()

                hq.heapify(current_orders)
                continue
            break
        return free_slot

    def distanceTimeCalc(self, order):
        return float(order.getDistance()*TIME_PER_KM_DISTANCE)

    #lookup
    def getSlotStatus(self):

        return self.kitchen_service.getSlotStatus()

