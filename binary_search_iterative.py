def binary_search1(input_array, value):
    """Your code goes here."""
    temp = input_array[:]
    while len(input_array) != 0:
        index  = (len(input_array)-1)/2
        middle = input_array[index]
        if value == middle:
            return temp.index(middle)
        elif value > middle:
            input_array = input_array[index+1:]
        elif value < middle:
            input_array = input_array[:index]
    return -1