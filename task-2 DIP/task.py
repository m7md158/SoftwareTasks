from abc import ABC, abstractmethod

# abs class
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass
    

# App = low level
## app1
class PayPalProcessor(PaymentProcessor):
    def pay(self, amount: float):
        print(f"Paying {amount} using PayPal.")
        
## ap2 
class VisaProcessor(PaymentProcessor):
    def pay(self, amount: float):
        print(f"Paying {amount} using Visa.")
        
 
 
# High level class       
class CheckoutService:
    def __init__(self, processor: PaymentProcessor):
        self.processor = processor

    def checkout(self, amount: float):
        self.processor.pay(amount)




checkout = CheckoutService(PayPalProcessor())
checkout.checkout(99.99)
