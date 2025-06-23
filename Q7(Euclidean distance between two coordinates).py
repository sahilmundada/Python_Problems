#Q7
#Euclidean distance between two coordinates.
import math as mt
class Distance:
    def __init__(self,num1_x,num1_y,num2_x,num2_y):
        self.num1_x=num1_x
        self.num1_y=num1_y
        self.num2_x=num2_x
        self.num2_y=num2_y

    def Find(self):
        distance = mt.sqrt((self.num2_x - self.num1_x)**2 + (self.num2_y - self.num1_y)**2)
        print("Euclidean distance between {},{} and {},{} is {}".format(self.num1_x,self.num1_y,self.num2_x,self.num2_y,distance))


print("Enter the two coordinates of which you want to find the distance")
a=int(input("Enter the x coordinate of 1st number :"))
b=int(input("Enter the y coordinate of 1st number :"))  
c=int(input("Enter the x coordinate of 2st number :"))
d=int(input("Enter the y coordinate of 2st number :"))    

A=Distance(a,b,c,d)
A.Find()