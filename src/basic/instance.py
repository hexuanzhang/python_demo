# 对象类型判断
import types

print(dir(types))
print('------')

## type()
print(type(123))   # <class 'int'>
print(type(1.5))   # <class 'float'>
print(type(4+5j))  # <class 'complex'>
print(type('123')) # <class 'str'>
print(type(True))  # <class 'bool'>
print(type(None))  # <class 'NoneType'>
print(type([]))    # <class 'list'>
print(type(()))    # <class 'tuple'>
print(type({}))    # <class 'dict'>
print(type(type))  # <class 'type'>
print(type(abs))   # <class 'builtin_function_or_method'>

print(type(123) in (int, str)) # true

def fn():
    pass
print(type(fn) == types.FunctionType) # True
print(type(abs) == types.BuiltinFunctionType) # True
print(type(lambda x: x) == types.LambdaType) # True
print(type((x for x in range(10))) == types.GeneratorType) # True

class Person():
    name = 'demo'
print(type(Person())) # <class '__main__.Person'>

print('------')

## isinstance()
print(isinstance('a', str)) # True
print(isinstance(123, int)) # True
print(isinstance(b'a', bytes)) # True
print(isinstance([1, 2, 3], (list, tuple))) # True
print(isinstance((1, 2, 3), (list, tuple))) # True

print('------')

# 对比
class BaseCls():
    pass

class TestCls(BaseCls):
    def __init__(self):
        pass

print(isinstance(TestCls(), BaseCls)) # True
print(type(TestCls()) == BaseCls) # False
print(type(TestCls()) == TestCls) # True