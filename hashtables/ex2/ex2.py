#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # route = []
    # d = {}
    # start = ""
    # for ticket in tickets:
    #     # print(ticket.source, ticket.destination)
    #     if ticket.source == 'NONE':
    #         start = ticket.destination
    #         route.append(start)
    #         print(start)
    #     elif ticket.destination == 'NONE':
    #         end = ticket.destination
    #         print(end)
    #     elif ticket.source == start:
    #         start = ticket.destination
    #         route.append(start)
    #     else:
    #         d[ticket.source] = ticket.destination

    # print("d", d)

    route = [None] * length 
    d ={}
    for ticket in tickets:
        # check for the start destination of our trip
        if ticket.source == "NONE":
            # add it to our `route` array as the first element
           route[0] = ticket.destination
        else:
            # hash each ticket with the source as key and destination as value
            d[ticket.source] = ticket.destination
      #If the tickets are greater than 1 then we need to check other wise we know our flight path.       
    if length > 1:
        # loop through our object, grabbing the source's associated destination and adding it to our route
        for i  in range(1, length):
            route[i] = d[route[i-1]]
        

    # print(length)
    # print(d)

    return route

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

print(reconstruct_trip(tickets, 10))

'''
Understanding:
    objective: reconstructe the trip based of the tickets
    -each ticket has a source and destination property
    -source = starting point
    -destination = end point
    each source will have a matching destination except for the initial start and final destination 

    - First flight has a source of None 
    -Last flight has a destination of None

    tickets = a list of ojbects that are tickets
    length = the lenght of the list

Planning:
    find start = ticket.source = None
    find end = tickt.destination = None
    path in between ticket.destination = ticket.source: append to list



'''