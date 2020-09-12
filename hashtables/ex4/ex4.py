def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    # create a cache with array values as keys
    num_dict = dict.fromkeys(a)

    # loop through initial array
    for i in a:
        # check if value has a negative counterpart in the cache
        if -i in num_dict and i > 0:
            result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
