
import os
from threading import Thread


class InputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(InputData):

    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'rb') as handle:
            return handle.read()

    @classmethod
    def generate_inputs(cls, config):
        """ Generic version of generate_inputs"""
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


def generate_inputs(data_dir):
    """ Original version of generate_inputs"""
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        """ Generic version of create_worker"""
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


def create_worker(input_list):
    """ Original version of create_worker"""
    workers = []
    for input_data in input_list:
        workers.append(LineCounter(input_data))
    return workers


class LineCounter(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count(b'\n')
        pass

    def reduce(self, other):
        self.result += other.result
        pass


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    first, rest = workers[0], workers[1:]
    for other in rest:
        first.reduce(other)
    return first.result


def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_worker(inputs)
    return execute(workers)


import random
from backports.tempfile import TemporaryDirectory


def write_test_files(temp_dir):
    for i in range(100):
        with open(os.path.join(temp_dir, str(i)), 'w') as handle:
            handle.write('\n' * random.randint(0, 100))


with TemporaryDirectory() as temp_dir:
    write_test_files(temp_dir)
    line_count = mapreduce(temp_dir)
    print line_count

