class Factorial:
  def __init__(self):
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

  
factorial_of = Factorial().__call__
print(factorial_of(5))
# I inputed 5