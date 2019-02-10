
NUMBERS = [8, 3, 1, 2, 5, 4, 7, 6]
GROUP = {2, 3, 5, 7}


def sort_priority(numbers, group):
    """ Sort the input numbers but put those in "group" first.

    :param numbers: list of input numbers.
    :param group: set of numbers in priority group.
    :return: True if any number in priority is found.
    """
    found = False

    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found


def main_original():
    numbers = NUMBERS[:]
    print(sort_priority_python_2(numbers, GROUP))
    print(numbers)


def sort_priority_python_3(numbers, group):
    """ Sort the input numbers but put those in "group" first.

    :param numbers: list of input numbers.
    :param group: set of numbers in priority group.
    :return: True if any number in priority is found.
    """
    found = False

    def helper(x):
        if x in group:
            nonlocal found
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found


def sort_priority_python_2(numbers, group):
    """ Sort the input numbers but put those in "group" first.

    :param numbers: list of input numbers.
    :param group: set of numbers in priority group.
    :return: True if any number in priority is found.
    """
    found = [False]

    def helper(x):
        if x in group:
            found[0] = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found[0]


if __name__ == '__main__':
    main_original()
