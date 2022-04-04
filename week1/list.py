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

def while_loop(i): 
    while i < len(InfoDb):
        print(InfoDb[i])
        i += 1
  
def recursive_loop(current_index):
  print(InfoDb[current_index])  
  if (current_index == len(InfoDb)-1):
    return
  else:
    recursive_loop(current_index+1)

def driver():
  print("For loop")
  for_loop()

  print("While loop")
  while_loop(0)#need to initialize i as 0

  print("Recursive loop")
  recursive_loop(0) #need to initialize i

if __name__ == "__main__":
    driver()