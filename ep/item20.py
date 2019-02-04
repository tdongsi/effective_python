
class Resistor(object):

    def __init__(self, ohms):
        self.ohms = ohms


class LoudResistor(Resistor):

    def __init__(self, ohms):
        super(LoudResistor, self).__init__(ohms)

    @property
    def ohms(self):
        print('Getter')
        return self._ohms

    @ohms.setter
    def ohms(self, value):
        print('Setter')
        self._ohms = value


def main():
    res = Resistor(1e3)
    print(res.ohms)
    res.ohms += 2e3
    print(res.ohms)

    res2 = LoudResistor(1e3)


if __name__ == '__main__':
    main()
