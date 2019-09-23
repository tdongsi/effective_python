"""
From the talk "Lack of Design Patterns in Python".

Example classes, objects, methods for each pattern follow this convetion: PatternName_ObjectName.
Example: Observer_A, FactoryMethod_Hello
"""
# Observer pattern can be achieved with decorator
def observer(f):
    def wrapper(self):
        print("f is called")   # observation
        return f(self)
    return wrapper


class Observer_A(object):
    @observer
    def f(self):
        return "Hello"


observer_a = Observer_A()
observer_a.f()


# Factory Method pattern: create objects of different classes based on an input string
# Abstract Factory pattern: factory of factories
class FactoryMethod_A(object):
    att = "Hello"


class FactoryMethod_B(object):
    att = "World"


factory_method = {
    "greeting": FactoryMethod_A,
    "subject": FactoryMethod_B
}

print factory_method["subject"]().att
