#Q8
#Triangle will form or not by giving the angle input and also what is the type of a triangle

class Shape:

    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def Check(self):
        if self.a+self.b+self.c==180:
            return True
        else:
            return False

    def Type(self):
        tri=self.Check()
        if tri==True:
            if self.a==self.b==self.c:
                print("It will form an Equilateral triangle")
            elif(self.a==self.b or self.c==self.b or self.a==self.c):
                print("It will form an Isoceles triangle")
            else:
                print("It will form an Scalene triangle")

        else:
            print("It will not form triangle")  

print('''Enter "1" to check weather it will form a triangle or not
Enter "2" to find the type of triangle : ''')   

enter=int(input("Enter your choice :"))               

if enter==1:
    print("Enter the angles of triangle")
    a=int(input("Enter the first angle :"))
    b=int(input("Enter the second angle :"))
    c=int(input("Enter the third angle :"))
    A=Shape(a,b,c)
    B=A.Check()
    if B==True:
        print("It will form a triangle")
    else:
        print("It will not form a triangle")

else:
    print("Enter the angles of triangle")
    a=int(input("Enter the first angle :"))
    b=int(input("Enter the second angle :"))
    c=int(input("Enter the third angle :"))   
    A=Shape(a,b,c)
    A.Type()


        