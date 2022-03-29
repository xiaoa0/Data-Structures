def fibonacci():
    a = int(input("How many terms? "))
    while (a > 20 or a <= 2): #need at least 2 terms to form sequence, setting limit as 20 for practicality reasons
      n = int(input("Please provide a valid input: ")) # checking input

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

fibonacci() #calling