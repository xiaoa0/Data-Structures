def factorial1(n): #need different function/class names otherwise it won't work
  result = 0 #initializing result as 0
  if n==1: 
    return 1
  else:
    return n * factorial1(n-1) #recursive loop, multiplying n by (n-1) 

print("Imperative factorial function: 7! = ",factorial1(7))

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
print("OOP factorial function: 5! = ",factorial_of(5))
# set 5 as value beforehand, not taking user input