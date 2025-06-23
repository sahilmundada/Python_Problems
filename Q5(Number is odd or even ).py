#Q5
#Number is odd or even

class Number():

    def __init__(self,num):
        self.num=num

    def check(self):
        if self.num%2 == 0:
            print("{} is a even number ".format(self.num))
        else:
            print("{} is a odd number".format(self.num))    
    
enter=int(input("Enter the number which you wanna have to check:"))
A=Number(enter)
A.check()    