def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight = {}
    duplicates = {}
    duplicates_check = False
    for x in range(length):
        current = weights[x]
        weight[current] = x
        target = limit - current
        if target in weight:
            if current > target or current < target:
                return (x, weight[target])
            elif target == current:
                if duplicates_check is False:
                    duplicates_check = True
                    duplicates[current] = x
                elif duplicates_check is True:
                    return (x, duplicates[current])
    return None


'''
Understanding
-given a weight limit as the limit argument: number/int
-given a list of weights as the weights argument: list/aarray 

Create a function that returns the sum of two weights that equal the weight limit. 

it will return Answer as a tuple that has two index's of the weights list. The greater of the two indexs goes fires. 

if there isn't a pair that exists then return none. 

Planning: 
-create a dictionary called d
-key to be weight and the value to be the index in the weights list. 

- add together the keys to see if they add up to the limit. 
-if they do return a tuple with index's in it
- else return none. 
'''


