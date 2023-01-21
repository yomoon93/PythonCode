class Trade (object):
    def __init__(self,id,symbol,quantity,price = 0.0):
        self.id = id
        self.symbol = symbol
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return "Trade : ID: " + str(self.id)+", Symbol: "+str(self.symbol)+ ", Quantity: "+str(self.quantity)+ ", Price: " + str(self.price)

    def getValue(self):
        return self.price * self.quantity

t=Trade("T1", "PPL", 100,15.25)
print(t)
t2 = Trade("T2","AMZ",100)
print(t2)
t2.price = 111.57
print(t2)

print(t2.getValue())