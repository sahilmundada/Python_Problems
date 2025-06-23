#Q4
#reverse a four digit number,check whether the reverse is true

class Reverse:

    def __init__(self,num):
        self.num=num

    def FindTheReverse(self):
        b=0
        a=self.num
        while a>0:
            b=b*10
            b=a%10+b
            a=a//10
        return b   

class Check:

    def __init__(self,num,num_rev):
        self.num=num
        self.num_rev=num_rev

    def check(self):
        A=Reverse(self.num)
        if A.FindTheReverse() == self.num_rev:
            print("Yes,the number are reverse of each other!!")
        else:
            print("No,the numbers are not reverse of each other!!")    

print('''Choose your option
      Enter "1" to find the reverse of the number
      Enter "2" to check weather the numbers are reversely same or not''')
entry=(int (input("Enter your choice here :")))

if entry==1:
    a=int(input("Enter the number:"))
    R=Reverse(a)
    print(R.FindTheReverse())
else:
    a=int(input("Enter the number :"))
    b=int(input("Enter the reverse number of it :"))
    C=Check(a,b)
    C.check()

                