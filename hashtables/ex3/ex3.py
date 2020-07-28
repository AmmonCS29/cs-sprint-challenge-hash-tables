def intersection(arrays):
    """
    YOUR CODE HERE
    Understand:
        objective: find the number(s) that exist in all lists adn return it
        - Find the intersection of multiple list ofintergers. 
        - Lists of lists that contain integers. 
        - find the numbers that exist in all the lists
    Planning: 
    -create a dictionary
    -some how iterate over first. input those as numbers as keys and the value to be 0
    -if the key is in the next list the value = 1 otherwise it stays 0

    """
    # Your code here
    d = {}
    result= []
    # if arrays in d:
    for x in arrays: # x is a single list
        for j in x: # j is a item in the list x
            if j not in d: #if j is not in dicitionary d
                d[j] = 0 # j = key and 0 he value
            else:
                result.append(j) # append j to the result list
    result= list(dict.fromkeys(result)) # removes duplicts out of the list and creates a new list
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
