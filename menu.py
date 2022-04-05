#importing files
from week0 import animation, swap
from week1 import fibonacci, list
from week2 import factorial, math

# Menu list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. "filename.py" will be run by exec(open("filename.py").read())
# 2. file.function references will be executed as file.function()
week0_menu = [
    ["Animation", animation.driver],
    ["Swap", swap.driver],
]

week1_menu = [
    ["Fibonacci", fibonacci.driver],
    ["Lists and Loops", list.driver],
]

week2_menu = [
    ["Factorial", factorial.driver],
    ["Math (Factors)", math.driver],
]


def menu(title, options):
    # header for menu
    # Menu banner
    border = "=" * 25
    banner = f"\n{border}\n{title}\n{border}"
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    menu(title, options)  # recursion, start menu over again


# def week0 menu
def _week0_menu():
    title = "Week 0"
    menu(title, week0_menu)

# def week1 menu
def _week1_menu():
    title = "Week 1"
    menu(title, week1_menu)


# def week2 menu
def _week2_menu():
    title = "Week 2"
    menu(title, week2_menu)

#driver to run
def driver():
    title = "Main Menu"
    menu_list = [["Week 0", _week0_menu],
                 ["Week 1", _week1_menu],
                 ["Week 2", _week2_menu]]
    menu(title, menu_list)


if __name__ == "__main__":
    driver()