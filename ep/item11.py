def index_words(text):
    """Find indices of all words in the input string."""
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index+1


def index_words_typical(text):
    """Find indices of all words in the input string."""
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result


def index_words_stream(handle):
    """Find indices of all words in input file stream."""
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


address = 'The quick brown fox jumps over the lazy dog'
print(list(index_words(address)))
print(index_words_typical(address))
