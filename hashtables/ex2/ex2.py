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
    ticket_dict = {}
    organized_routes = []

    # iterate over all of the tickets and add to the dictionary
    # map ticket source to key and destination to value
    for ticket in tickets:
        ticket_dict[ticket.source] = ticket.destination

    # start with the value of the dict at source == NONE
    # for first flight
    destination = ticket_dict["NONE"]

    # go until destination equals NONE
    while destination != "NONE":
        # add the destination to the organized flights
        # then reassign destination to be the next value
        organized_routes.append(destination)
        destination = ticket_dict[destination]

    # tests require that NONE be added at the end
    organized_routes.append(destination)

    return organized_routes
