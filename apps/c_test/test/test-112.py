from .test_113 import name

print(name)

try:
    assert 1 == 2
except Exception as e:
    print(type(e))
    print(e)


