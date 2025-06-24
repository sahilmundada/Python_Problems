#Q28
#Number is prime number or not

class Number:

    def __init__(self,num):
        self.num=num

    def Is_Prime(self,n=None):
        if n is None:
           n=self.num 
        for i in range(2,((n)//2)+1):
            if n%i==0:
                return False
            
        return True        

    def First_N_Prime(self):
        count=0
        number=3
        while(count<self.num):
            if self.Is_Prime(number)==True:
                print(number,end=" ")
                number+=1
                count+=1
            else:
                number+=1    
        
enter=int(input("Enter the number :"))
A=Number(enter)
#To find the number is prime or not
if A.Is_Prime():
    print("Enter Number {} is a Prime Number".format(enter))
else:
    print("Enter Number {} is not Prime Number".format(enter))

#To print N prime number
A.First_N_Prime()

           