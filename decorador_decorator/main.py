# decorator function
def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print('wrapped executed before {}()'.format(original_func.__name__))
        return original_func(*args,**kwargs)
    return wrapper_func

# decorator class
class DecoratorClass(object):

    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print('call method executed before {}()'.format(self.original_func.__name__))
        return self.original_func(*args,**kwargs)

# functions
def display():
    print("display function ran")

@decorator_func
def display_info(name, age):
    print("My name is {} and i'm {} years old".format(name, age))

@DecoratorClass
def other_display():
    print("other display function ran")

decorated_display = decorator_func(display)
decorated_display()

other_display() 
display_info('fabian', 12)