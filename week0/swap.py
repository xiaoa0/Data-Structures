def swap(a, b): #function logic
    print("Original: ",a, b)
    if (a > b or a < b): #doing the swap when the two numbers aren't equal
        temp = a
        a = b
        b = temp
        print("Swapped: ",a, b)
    else: #just returning the numbers in same order b/c they're equal, no need to swap
      print("No swap: ",a, b)

def driver():
    # setting parameters for different decisions by function
    swap(10, 1)
    swap(5,5)
    swap(3,7)

    swap("aaa", "aaa")
    swap("aaa", "bbb")
    swap("bbb", "aaa")

if __name__ == "__main__":
    driver()