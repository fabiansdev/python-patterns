from functools import wraps

def check_float(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        for i in args:
            if isinstance(i, float) == False:
                print("{} is not a float".format(i))
        return orig_func(*args, **kwargs)
    return wrapper

def check_string(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        for i in args:
            if isinstance(i, str) == False:
                print("Fuck off nigga, this {} is not a string".format(i))
        return orig_func(*args, **kwargs)
    return wrapper

@check_string
@check_float	
def calculate_sum(*args):
    print(sum(args))
    return sum(args)

calculate_sum(1,2,3)
calculate_sum(2,4,6)
