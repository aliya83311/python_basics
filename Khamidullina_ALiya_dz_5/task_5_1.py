def odd_nums(end):
    """ Form an iterable consisting of odd numbers.

    :param end: an integer representing the highest value in the iterable
    :return: the iterable of odd numbers starting from 1 and including end value
    """
    try:
        end = int(end)
    except ValueError:
        print("This function takes only integers.")
    else:
        for n in range(1, end + 1, 2):
            yield n


odd_35 = odd_nums(input("Type any number: "))
print(next(odd_35))
print(next(odd_35))
print(next(odd_35))
