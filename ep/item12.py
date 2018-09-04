
def normalize_data(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')

    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100.0 * value / total
        result.append(percent)
    return result


path = '/tmp/my_numbers.txt'
with open(path, 'w') as f:
    for i in [15, 80, 35]:
        f.write('%d\n' % i)


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


print(normalize_data([15, 80, 35]))
# print(normalize_data(read_visits(path)))


def normalize_data_2(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100.0 * value / total
        result.append(percent)
    return result

get_iter = lambda: read_visits(path)
print(normalize_data_2(get_iter))


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


visits = ReadVisits(path)
print(normalize_data(visits))
