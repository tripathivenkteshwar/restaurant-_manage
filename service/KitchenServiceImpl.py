from service.KitchenService import KitchenService
from models.Kitchen import Kitchen
import heapq as hq

class KitchenServiceImpl(KitchenService):
    kitchenOrderList = []
    slotAvailable = 7
    kitchen_time_wait = 0.0

    def updateKitchenTimeWait(self, time):
        self.__class__.kitchen_time_wait = float(time)

    def getKitchenTimeWait(self):
        return self.__class__.kitchen_time_wait

    def addOrders(self, order, time, slot):
        time = float(time + self.__class__.kitchen_time_wait)
        kitchen = Kitchen(order, time, slot)
        order.setOrderTime(time)

        self.__class__.kitchenOrderList.append(kitchen)

        self.__class__.slotAvailable = self.__class__.slotAvailable - slot
        hq.heapify(self.__class__.kitchenOrderList)

    def setSlotStatus(self, slot):
        self.__class__.slotAvailable = self.__class__.slotAvailable + slot

    def getSlotStatus(self):
        return self.__class__.slotAvailable

    def getCurrentOrders(self):
        hq.heapify(self.__class__.kitchenOrderList)
        return self.__class__.kitchenOrderList

    def getCurrentOrderById(self, id):
        pass

# class chkS:
#     def __init__(self, f, val):
#         self.f=f
#         self.val=val
#     def __lt__(self, other):
#         return self.val<other.val
# class chk:
#     l=[]
#     def add(self, f, val):
#         self.__class__.l.append(chkS(f, val))
#         self.__class__.l.append(chkS("rr", val+45))
#         self.__class__.l.append(chkS("jj", val-7))
#         self.__class__.l.append(chkS("jj", val-15))
#         self.__class__.l.append(chkS("kk",  val+5))
#         hq.heapify(self.__class__.l)
#
#     def ret(self):
#         hq.heapify(self.__class__.l)
#         return self.__class__.l
# if __name__ == '__main__':
#     print("hello")
#     k = KitchenServiceImpl()
#     k.addOrders("a", 5, "q")
#     k.addOrders("b", 10, "w")
#     k.addOrders("c", 3, "e")
#     k.addOrders("s", 19, "k")
#     k.addOrders("t", 37, "kl")
#     k.addOrders("l", 4, "ka")
#     l=k.getCurrentOrders()
#     # print(k.kitchenOrderList)
#     for i in range(len(l)):
#         print(l.pop(0).getKitchenTime())
#
#         hq.heapify(l)
#         if l:
#             print(l[0].getKitchenTime(),"test")

    # ch=chk()
    # ch.add("lu",25)
    # lll=ch.l
    # print(lll)
    # for i in lll:
    #     print(i.val)
    #
    # print("ckk")
    # chll=ch.ret()
    # for i in chll:
    #     print(i.val)
    # print("lllllll")
    # # for i in range(len(ch)):
    # #     print(i.pop().val)

    # ch=chk()
    # ch.add("lu",25)
    # for i in ch.l:
    #     print(i.val)
    # print("lllllll")
    # for i in range(len(ch.l)):
    #     print(ch.l.pop(0).val)
    #     hq.heapify(ch.l)