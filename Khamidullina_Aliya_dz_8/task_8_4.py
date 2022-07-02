from functools import wraps


def val_check(check):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            if check(*args):
                return func(*args)
            else:
                raise ValueError(f"wrong value {args}")

        return wrapper

    return decorator


@val_check(check=lambda x: isinstance(x, int))
def calc_cube(x):
    return x ** 3


print(calc_cube.__name__)
print(calc_cube(5))
print(calc_cube("5"))
