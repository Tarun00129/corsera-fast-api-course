# type-hint is a process or a practice of adding type after the variable name
# it is used to make the code more readable and maintainable
# it is also used to make the code more type-safe
# it is not mandatory to use type-hint in python
# but it is recommended to use type-hint in python

# example of type-hint

text: str = "Hello World"
number: int = 10
pi: float = 3.14
is_active: bool = True

print(type(text))
print(type(number))
print(type(pi))
print(type(is_active))

# list

numbers: list[int] = [1, 2, 3, 4, 5]
print(type(numbers))

# tuple

coordinates: tuple[int, int] = (1, 2)
print(type(coordinates))

# dictionary

person: dict[str, int] = {"name": "John", "age": 30}
print(type(person))

# set

my_set: set[int] = {1, 2, 3, 4, 5}
print(type(my_set))


# function
# -> is used to specify the return type so this code will return an integer value
def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))
