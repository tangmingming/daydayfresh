
def decorator(prefix):
  def decorator_2(s_f):
    def ret_func(*args, **kwargs):
      ret = s_f(*args, **kwargs)
      print("{}:{}".format(prefix, ret))
      return ret
    return ret_func
  return decorator_2

@decorator("ret=")
def add(x, y):
  return x*y

add(2, 3)
