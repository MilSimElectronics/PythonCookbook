def welcome():
    """Multi-line comment"""
    print("Welcome")


def required_parameters(name, greeting):
    print(greeting + ", " + name)


def optional_parameters(name, greeting="Welcome... "):
    print(greeting + name)


def return_value(base_number):
    cube_value = base_number * base_number * base_number
    return cube_value


welcome()
required_parameters("Carlos", "Greeting")
optional_parameters("Carlos")
the_value = return_value(3)
print(the_value)

