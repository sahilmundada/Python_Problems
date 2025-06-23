#Q2
#Convert celsius value to fahrenheit
class Temp:
  def __init__(self,celsius):
    self.celsius=celsius

  def CelToFah(self):
    F = (self.celsius * 9/5) + 32
    return F

cel=int(input("Enter the temp in celsisus:"))
temp=Temp(cel)
print("Converted to fahrenheit:",temp.CelToFah())    