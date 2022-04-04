#importing other files to run

from week0 import animation, swap
from week1 import fibonacci, lists
from week2 import factorial, math

main_menu = [
    
]

#week 0
week0_menu = [
    ["Animation", animation.driver],
    ["Swap", swap.driver],
]

#week 1
week1_menu = [
  ["Fibonacci", fibonacci.fibonacci],
  #["List", lists.],
]

#week 2
week2_menu = [
  ["Factorial", factorial.factorial1],
  #["OOP Factorial", factorial.factorial],
  ["Factors", math.factors],
  #["OOP Factors", math.],
]

#submenu for list loops
list_menu = [
  ["For loop", lists.for_loop],
  ["While loop", lists.while_loop],
  ["Recursive loop", lists.recursive_loop(0)],
]


border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def menu():
    title = "Menu" + banner
    main_menu.append(["Week 0", week0_menu])
    main_menu.append(["Week 1",week1_menu])
    main_menu.append(["Week 2",week2_menu])
    buildMenu(title, main_menu)

def week0_menu():
  title = "Week 0 Menu" + banner
  buildMenu(title, week0_menu)
  
def week1Menu():
  title = "Week 1 Menu" + banner
  week1_list.append(["Different loops", list_menu],)
  buildMenu(title, week1_menu)

def week2Menu():
  title = "Week 2 Menu" + banner
  buildMenu(title, week2_menu)

def list_menu():
  title = "List Menu" + banner
  buildMenu(title, list_menu)

def buildMenu(banner, options):

    print(banner)

    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    for key, value in prompts.items():
        print(key, '->', value[0])


    choice = input("Type your choice> ")


    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")

    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")


    buildMenu(banner, options) 


if __name__ == "__main__":
    menu()