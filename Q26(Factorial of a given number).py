#Q26
#Factorial of a given number

class Number:

    def __init__(self,num):
        self.num=num

#Function without recursion
    def fact(self):
        factorial=1
        for i in range(1,self.num+1):
            factorial=factorial*i 
        return factorial  
    
#Function with recursion
    def fact(self,n=None):
        if n is None:
            n=self.num
        if n==1 or n==0:
            return 1
        else:
            return n*self.fact(n-1)     

#Normal Fuction with recursion
# def fact(num):
#     if num==1 or num==0:
#         return 1
#     else:
#         return num*fact(num-1)

enter=int(input("Enter the number to find the factorial :"))
A=Number(enter)
print(A.fact(enter))            