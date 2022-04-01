def swap():
    x = int(input('input a number '))
    y = int(input('input a number '))
    x,y = swap2(x, y)
    print(x,y)
  
def swap2(a, b):
    if (a > b or a == b):
        temp = a
        a = b
        b = temp
        return a, b

