def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_dict = {}

    for i in range(length):
        # get the difference of limit and weight
        diff = limit - weights[i]
        # check to see if diff is in weight_dict 
        if diff in weight_dict:
            # compare higher index and return
            if weight_dict[diff] > i:
                return (weight_dict[diff], i)
                
            else:
                return (i, weight_dict[diff])
        
        else:
            weight_dict[weights[i]] = i
        


    return None

get_indices_of_item_weights([1, 2, 4, 6], 4, 10)











# records = [
#     ("Tim", "Austin", "December"),
#     ("Jerimiah", "Redmond"),
#     ("Paul", "Los Angeles"),
#     ("Ryan", "Austin"),
#     ("Tucker", "Asheville"),
#     ("Ari", "San Jose")
# ]

# d = {}
# for record in records:
#     city = record[1]
#     name = record[0]
#     if city in d:
#         d[city].add(name)
#     else:
#         d[city] = set()
#         d[city].add(name)
# print(d["Austin"])
# print(d["Redmond"])