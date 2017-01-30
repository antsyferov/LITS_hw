def type_check(arg_type=None):
    arg_type = arg_type or str
    def actual_decorator(func):
    
        def wrapper(*args, **kwargs):
            if not all([isinstance(arg, arg_type) for arg in args]):
                raise Exception('Invalid arg for type {}'.format(arg_type))
            res = func(*args, **kwargs)
            return res

        return wrapper
    return actual_decorator

def to_int(func):
    
    def wrapper(*args, **kwargs):
        args = [int(arg) for arg in args]
        res = func(*args, **kwargs)
        return res

    return wrapper

    
@to_int
@type_check(int)
def summ(a, b):
    return a + b

@type_check()
def summ_str(a, b):
    return a + b

print(summ_str('1', '3'))
print(summ('1', 3))
