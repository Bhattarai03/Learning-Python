# Write a class Train which has methods to book a ticket ,get status (no. of seats ) and get fare( information of train running under indian railways).
class Train():

    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fro,to):
         print(f"Ticket is booked in train No: {self.trainNo}\n From {fro} To {to}")

    def getstatus(self,):
        print(f"The train {self.trainNo } is running on time")
    def getfare(self,fro,to,price):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {price}")
        

t=Train(12)

t.book("Itahari ","Biratnagar")
t.getstatus()
t.getfare("Itahari","Biratnagar",1500)

        


    