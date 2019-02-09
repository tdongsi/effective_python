
meep = 23


def enclosing():
    """ Variable reference in different scopes.

    When referring to a variable not existing in the inner scope,
    Python will try to look up in the outer scope.
    """
    foo = 15

    def my_func():
        bar = 10

        print(bar)      # local scope
        print(foo)      # enclosing scope
        print(meep)     # global scope
        print(str)      # built-in scope
        # print(does_not_exist)

    my_func()


enclosing()


def enclosing_assignment():
    """ Variable assignment in different scopes.

    Different from variable reference.
    When assigning to a variable not existing in the inner scope,
    Python will create a new local variable.
    """

    foo = 15
    foo = 25

    def my_func():
        foo = 15
        bar = 5

        print(foo)
        print(bar)

    my_func()
    print(foo)
    # print(bar)   # Does not exist


enclosing_assignment()
