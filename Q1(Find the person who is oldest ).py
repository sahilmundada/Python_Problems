#Q1
#Find the person who is oldest 
class old:
  def __init__(self,age1,age2,age3):
    self.age1=age1
    self.age2=age2
    self.age3=age3

  def find_old(self):  
    max_age=max(age1,age2,age3)
    print("The Oldest one is {} person".format(max_age))

per=old
age1=int(input("Enter the age of first person:"))
age2=int(input("Enter the age of second person:"))
age3=int(input("Enter the age of third person:"))
per=old(age1,age2,age3)
per.find_old()


