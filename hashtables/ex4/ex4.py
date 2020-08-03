def has_negatives(a):
    """
    YOUR CODE HERE
    """
    d = {} # dictionary
    result = [] # list to return results
    for num in a: # if the num has a corrisponding number in the dictionary
        if d.get(abs(num)): # .get method returns the value for the given key
            result.append(abs(num)) #append the results to the list
        else:
            d[abs(num)] = num #if no value is found pass dict a new key along with its value. 
    return result
if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
