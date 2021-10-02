class Atm:
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber
    def CheckBalance(self):
        print("Your Balance is 50,000")
    def Withdrawl(self,amount):
        newamount=50000-amount
        print("You have withdran amount"+ str(amount)+"Your Remaining Balance is"+ str(newamount))
def main():
    cardnumber=input("Enter Your Card Number")
    pinnumber=input("ENter your Pin Number")       
    user=Atm(cardnumber,pinnumber) 
    print("Choose Your Activity")
    print("1.Blanace Enquery 2.Withdrawl")
    Activity=int(input("Enter Your Activity Number"))
    if(Activity==1):
        user.CheckBalance()
    elif(Activity==2):
        amount=int(input("Enter The Amount"))
        user.Withdrawl(amount)
    else:
        print("Enter a Valid Number")
main()           


