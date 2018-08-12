
def main():
    names = ['Kelly', 'Lise', 'Marie', 'Alexander']
    letters = [len(e) for e in names]

    # Find the longest name

    # Worst way
    # Iterate for idx in range(len(names))

    # Bad way: use enumerate
    print bad_way(letters, names)

    # Better way: use zip
    print better_way(letters, names)

    # In Python2, zip returns a list instead of a generator.
    print zip(letters, names)
    # In Python3, the above will print some "<zip object at 0x12345>".

    # To get something similar to Python3,
    # Use izip in itertools
    print python3_way(letters, names)

    # Demo of izip_longest
    izip_longest()

    pass


def python3_way(letters, names):
    """Find the longest name"""
    from itertools import izip
    longest_name = None
    current_max = 0
    for length, name in izip(letters, names):
        if length > current_max:
            current_max = length
            longest_name = name
    return longest_name


def better_way(letters, names):
    """Find the longest name"""
    longest_name = None
    current_max = 0
    for length, name in zip(letters, names):
        if length > current_max:
            current_max = length
            longest_name = name
    return longest_name


def bad_way(letters, names):
    """Find the longest name"""
    longest_name = None
    current_max = 0
    for idx, e in enumerate(letters):
        if e > current_max:
            current_max = e
            longest_name = names[idx]
    return longest_name


def izip_longest():
    names = ['Kelly', 'Lise', 'Marie']
    letters = [len(e) for e in names]
    names.append('Alexander')

    from itertools import izip_longest
    for length, name in izip_longest(letters, names):
        if length is None:
            print "%s has unknown length" % name
        else:
            print "%s has %d characters" % (name, length)


if __name__ == '__main__':
    main()