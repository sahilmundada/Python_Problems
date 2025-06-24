class Number:

    def __init__(self, start, end=None):
        if end is None:
            self.start = self.end = start
        else:
            self.start = start
            self.end = end

    def is_armstrong(self, n=None):
        if n is None:
            n = self.start  # default to single value
        power = len(str(n))
        total = 0
        temp = n

        while temp > 0:
            digit = temp % 10
            total += digit ** power
            temp = temp // 10

        return total == n 
    
    def n_armstrong(self):
        print(f"Armstrong numbers from {self.start} to {self.end}:")
        for i in range(self.start, self.end + 1):
            if self.is_armstrong(i):
                print(i, end=" ")
        print()  # for a clean newline


enter = int(input("Enter a number to check: "))
A = Number(enter)
if A.is_armstrong():
    print(f"{enter} is an Armstrong number.")
else:
    print(f"{enter} is NOT an Armstrong number.")

# List all Armstrong numbers between 100 and 1000
print("\n--- Armstrong Numbers in Range 100 to 1000 ---")
B = Number(100, 1000)
B.n_armstrong()