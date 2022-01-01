def decorate(func):
    def inner():
        print("hi")
        func()
        print("bye")
    return inner

@decorate
def test():
    print("test")

test()

