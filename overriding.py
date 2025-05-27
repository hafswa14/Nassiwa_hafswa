class Payment:
    def process(self, amount):
        print(f"General {amount}Payment processing")

class DebitCard(Payment):
    def process(self, amount):
        print(f"Processed UGX {amount} via debit card")

class MobileMoney(Payment):
    def process(self, amount):
        print(f"Processed UGX {amount} via mobile money")
momo= MobileMoney()
momo.process(50000) 
      
        
