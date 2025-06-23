#Q3
#sum of 3 digits

class Sum:

    def __init__(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3

    def Total(self):
        #We cant use the sum function , it will take only two arguments 
        a=self.num1+self.num2+self.num3    
        return a

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))

A=Sum(num1,num2,num3)
print(A.Total())
        