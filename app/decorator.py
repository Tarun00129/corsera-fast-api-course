# this is a simple function which is used to print a message without any decorator function.
def log():
    print("Hii, My Name is Tarun")


log()

# lets create a decorator function


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()
