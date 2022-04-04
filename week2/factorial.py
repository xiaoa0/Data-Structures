#this is the imperative form
def factorial1(n): #need different function/class names otherwise it won't work
  result = 0 #initializing result as 0
  if n==1: 
    return 1
  else:
    return n * factorial1(n-1) #recursive loop, multiplying n by (n-1) 

class Factorial: #oop form
  def __init__(self): #initializing list with entry 1
    self.factorial = [1,]
  def __call__(self, n):
    if n < len(self.factorial):
      return self.factorial[n]
    else:
      # Compute the requested Fibonacci number
      factorial_number = self(n - 1) * n # two recursive calls to self (__call__(self, n))
      #To find the factorial of a number, multiply the number with the factorial value of the previous number
      self.factorial.append(factorial_number) # builds list, with most nested of the calculations 1st... may hurt your head
      return self.factorial[n]

def driver(): #driver sets number parameters for functions, in this case 4 for imperative gives 24 and 5 for OOP form gives 120
  print("Factorial (imperative): 4! = ",factorial1(4))

  factorial_of = Factorial().__call__
  print("Factorial (OOP): 5! = ",factorial_of(5))

if __name__ == "__main__":
    driver()