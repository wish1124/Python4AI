from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class NaverPay(Payment):

    def pay(self,amount):
        print(f"신용카드로 {amount}원 결제 완료")

pay = NaverPay()
pay.pay(30000)