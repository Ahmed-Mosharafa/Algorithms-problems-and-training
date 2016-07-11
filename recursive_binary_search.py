def binary_search(input_array, value):
    """Your code goes here."""
    input_array.sort()
    index = (len(input_array)-1) /2
    print "finally", index, input_array
    pivot = input_array[index]
    if value == pivot:
        return True
    elif value < pivot and len(input_array) > 1:
        return binary_search(input_array[:index], value)
    elif value > pivot and len(input_array) > 1: 
        print input_array, index       
        return binary_search(input_array[index+1:], value)
    else:
        return False