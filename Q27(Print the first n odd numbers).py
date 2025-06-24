#Q27
#Print the first n odd numbers

class Number:

    def __init__(self,num):
        self.num=num

    def First_N_Odd(self):
        for i in range(2,2*self.num+2):
            if i%2!=0:
                print(i,end=" ")
            else:
                continue

enter=int(input("Enter the number :"))
A=Number(enter)
A.First_N_Odd()