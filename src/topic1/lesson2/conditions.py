if __name__ == '__main__':
    x = 2
    print(x == 2)  # prints out True
    print(x == 3)  # prints out False
    print(x < 3)  # prints out True

    # Boolean operators
    name = "Oleg"
    age = 23
    if name == "Oleg" and age == 23:
        print("Your name is Oleg, and you are also 23 years old.")

    # The "in" operator
    name = "Alex"
    access_names = ["John", "Oleg", "Alex"]
    if name in ["John", "Oleg", "Alex"]:
        print("%s you have an access " % name)

    '''
    Unlike the double equals operator "==", the "is" operator does not match the values of the variables, 
    but the instances themselves. For example:
    '''
    x = [1, 2, 3]
    y = [1, 2, 3]
    print("x == y -", x == y)  # Prints out True
    print("x is y -", x is y)  # Prints out False
    print("x is x -", x is x)  # Prints out True

    '''
    Python uses indentation to define code blocks, instead of brackets. The standard Python indentation is 4 spaces, 
    although tabs and any other space size will work, as long as it is consistent.
    '''
    statement = False
    another_statement = True
    if statement is True:
        # do something
        pass
    elif another_statement is True:  # else if
        # do something else
        pass
    else:
        print("Both statements are False")
        pass


def conditions_task1():
    number = 10
    second_number = 10
    first_array = []
    second_array = [1, 2, 3]

    # TODO change the code
    if number > 1:
        print("1")

    if first_array:
        print("2")

    if len(second_array) == 2:
        print("3")

    if len(first_array) + len(second_array) == 5:
        print("4")

    if first_array and first_array[0] == 1:
        print("5")
