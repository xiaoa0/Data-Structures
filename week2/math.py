# Function to find the Factors of a Number
def findFactors(number):
    print("Factors of a Given Number {0} are:".format(number))
    for value in range(1, number + 1):
        if number % value == 0:
            print("{0}".format(value), end=" ")
    print()

def factors():
    num = int(input("(Imperative) Enter a number to find its factors: "))
    findFactors(num)

class Factoring: #oop form
  def __init__(self): #initializing list with entry 1 since 1 is factor for all numbers
    self.factoring = [ ]
  def __call__(self, n): #using call to make function-like object
      factor_number = 1 
      while factor_number <= n:
        if n % factor_number == 0:
          self.factoring.append(factor_number) # builds list, with most nested of the calculations 1st... may hurt your head
          factor_number = factor_number + 1
        else:
          factor_number = factor_number + 1
        
      return self.factoring

      

def driver():
  factors()

  factors_of = Factoring().__call__
  print("(OOP) The factors of 16 are: ",factors_of(16))

if __name__ == "__main__":
    driver()