# Function to find the Factors of a Number
def findFactors(number):
    print("Factors of a Given Number {0} are:".format(number))
    for value in range(1, number + 1):
        if number % value == 0:
            print("{0}".format(value), end=" ")
    print()

def factors():
    num = int(input("Enter a number to find its factors: "))
    findFactors(num)

def driver():
  factors()

if __name__ == "__main__":
    driver()
#need to initialize i as 0, add 1 to i each time 