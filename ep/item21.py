class ApiClass(object):

    def __init__(self):
        self.__value = 5

    def get(self):
        return self.__value


class Child(ApiClass):

    def __init__(self):
        super(Child, self).__init__()

        # Here, Child class author is not aware of
        # internal implementation of ApiClass
        # he accidentally override an internal attribute of ApiClass
        self._value = 'hello'

a = Child()
print(a.get())
