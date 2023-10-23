class fruits:
    def __init__(self,type,price,color):
        self.type = type
        self.price = price
        self.color = color
    def onyesha(self):
        print(f"I like eating {self.type} and it costs {self.price}, color being {self.color}")
myobj = fruits("banana" , "20 ksh" , "yellow")
myobj2 = fruits("mango","50 kshs","orange")
myobj.onyesha()
myobj2.onyesha()