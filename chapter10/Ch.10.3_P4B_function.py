python-book-samples $ python              
Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> def fn():
...     print("I am a function")
...     
>>> fn
<function fn at 0x10762bce0>
>>> id(fn), hex(id(fn))
(4418878688, '0x10762bce0')
>>> 
>>> type(fn)
<class 'function'>
>>> fn()
I am a function
>>> dir(fn)
['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__type_params__']
>>> fn.a = 33
>>> fn.a
33
>>> def donut():
...     print("I am Homer Simpson. I wasnt donuts.")
...     
>>> fn.f = donut
>>> fn.f()
I am Homer Simpson. I wasnt donuts.
>>> def donut():
...     print("I am Homer Simpson. I want donuts.")
...     
>>> fn.f = donut
>>> fn.f()
I am Homer Simpson. I want donuts.
>>> #We added 2 extra (arbitrary) attributes, a and f, to this object. a is a data attribute and f is a method.