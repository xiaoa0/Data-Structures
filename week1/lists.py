# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = [] #empty list

#adding 4 entries with student name, age, favorite subjects, and favorite cookie
InfoDb.append({  
  "Name": "Allie",  
  "Age": "16",
  "Subjects":["Physics","Computer Science","History"],
  "Favorite cookie": "Snickerdoodle"
              })  

InfoDb.append({  
  "Name": "Elizabeth",
  "Age": "15",
  "Subjects":["PE","Biology","Math"],
  "Favorite cookie": "Sugar"
              })  

InfoDb.append({
  "Name": "Ryan",
  "Age": "17",
  "Subjects":["Engineering","History","Art"],
  "Favorite cookie": "Chocolate chip"
})

InfoDb.append({
  "Name": "Alex",
  "Age": "13",
  "Subjects":["Tutorial","Lunch","Break"],
  "Favorite cookie": "Cookie dough"
})

# printing info from InfoDb with for loop, while loop, and recursive loop

def for_loop():
    for i in range(len(InfoDb)):
        print(InfoDb[i])

def while_loop():
    i=0
    while i < len(InfoDb):
        print(InfoDb[i])
        i += 1
  
def recursive_loop(p):
    if p < len(InfoDb):
        print(InfoDb[p])
        recursive_loop(p + 1)
    return

# selecting loop to run
def select_loop():
    choice = input("Choose loop: for, while, or recursive? ")
    while not (choice=="for") or (choice=="while") or (choice=="recursive"):
        choice = input("Please enter a valid input: ")
    if (choice == "for"):
        for_loop()
    elif (choice == "while"):
        while_loop()
    elif (choice == "recursive"):
        recursive_loop(p)

select_loop()