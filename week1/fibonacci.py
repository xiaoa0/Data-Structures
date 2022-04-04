def fibonacci(a):
    def sequence(s):
        if s <= 1: #for inital n=1
            return s
        else: #adding 2 previous terms
            return(sequence(s-1) + sequence(s-2))

    for index in range(a): #printing terms
        if index == range(a):
            print(sequence(index))
        else:
            print(sequence(index))

def driver():
  print("Fibonacci sequence up to 7th term: ")
  fibonacci(7)

if __name__ == "__main__":
    driver()