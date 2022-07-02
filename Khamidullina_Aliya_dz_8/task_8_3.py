from functools import wraps


def type_logger(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    for item in args:
      arg_type = type(item)
      temp = func(item)
      print(f"calc_cube({item}: {arg_type})", end=", ")
      print(f"result {temp}: {type(temp)}", end=", ")
    for key, value in kwargs.items():
      value_type = type(value)
      temp = func(value)
      print(f"calc_cube({key}: {value}: {value_type})", end=", ")
      print(f"result {key}: {temp}: {type(temp)}", end=", ")
  return wrapper


# @return_type
@type_logger
def calc_cube(x):
   return x ** 3


print(calc_cube.__name__)
print(calc_cube(2, 4, first=5))
