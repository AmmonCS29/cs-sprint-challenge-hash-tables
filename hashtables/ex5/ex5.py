# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE

    Understanding:
        - you files and quiries arguments
        - each is a list of strings
        Objective: to see if the query is in the file path. return the file paths that correspond with the quiries in a list format. 

    Planning:
        Files:
            -list of strings
            -split the string by the /
        Quieries:
            -list of strings
    """
    # Your code here
    result = []
    d= {}
    for f in files:
        x = f.split("/")
        y = x[-1] # y becomes the last value in the x list
        if y not in d:
            d[y] = [] #y becomes the key and an empty list is the value
        d[y].append(f) # if it is in the directory f is appended to the value list. 
    for query in queries:
        if query in d: # if the query is in the dictionary
            result.extend(d[query]) #extend the list in the dictionary to the result list. 
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
