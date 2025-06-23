#Q6
#Year is a leap year or not.

class Year:

    def __init__(self,num):
        self.num=num

    def Check(self):
        if self.num%4==0 and self.num%100!=0 or self.num%400==0:
            print("Enter year is a leap year")
        else:
            print("Enter year is not a leap year") 

enter=int(input("Enter the year which you wanna have to check:"))
A=Year(enter)
A.Check()                  