# Write a class Train which has methods to book a ticket ,get status (no. of seats ) and get fare( information of train running under indian railways).
class Train():
    def book(self,trainNo,fro,to):
         print(f"Ticket is booked in train No;{trainNo}\n From {fro} To {to}")

    def getstatus(self,trainNo):
        print(f"The train {trainNo } is running on time")
    def getfare(self,trainNo,fro,to,price):
        print(f"Ticket fare in train no: {trainNo} from {fro} to {to} is {price}")
        

t=Train()
t.book(12,"Itahari ","Biratnagar")
t.getstatus(12)
t.getfare(12,"Itahari","Biratnagar",1500)

        


    