# A = [2, 7, 2, 5]
# it = iter(A)

# try:
#     while True:
#         print(next(it))
# except StopIteration:
#     pass

# class MyListIterator:
#     def __init__(self, data):
#         self.i = -1
#         self.data = data

#     def __next__(self):
#         self.i += 1
#         if self.i >= len(self.data):
#             raise StopIteration
#         return self.data[self.i]

            
# class MyList:
#     def __init__(self):
#         self.data = []

#     def __iter__(self):
#         return MyListIterator(self.data)
    

# A = MyList()
# A.data = [2, 8, 9, -3]


# for element in A:
#     print(element)


# x = range(2, 10, 3)
# print(type(x))
# for i in x:
#     print(i)

# def natural_generator():
#     i = 0
#     while True:
#         i += 1
#         yield i

# for x in natural_generator():
#     print(x)


# def all_pairs(data):
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             yield data[i], data[j]


# for x, y in all_pairs([2, 8, 3, 9]):
#     print(x, y)


# def MyRange(start, finish=None, step=None):
#     if finish is None:
#         start, finish = 0, start
#     if step is None:
#         if finish >= start:
#             step = 1
#         else:
#             step = -1
#     curr = start
#     while (finish - curr) * (finish - curr + step) > 0:
#         yield curr
#         curr += step
        


# for x in MyRange(4, 3):
#     print(x)


# import time

# def wrapper(func):
#     def wrapped_func(*args, **kwargs):
#         print("begin decoration")
#         res = func(*args, **kwargs)
#         print("finish decoration")
#         return res

#     return wrapped_func

# def time_dec(func):
#     def wrapped_func(*args, **kwargs):
#         t = time.time()
#         res = func(*args, **kwargs)
#         t = time.time() - t
#         return {"res": res, "time_duration": t}
    
#     return wrapped_func


# @time_dec
# def MyFunc(x):
#     print(f"my func with {x}")


# x = MyFunc(3)
# print(x)


# def fib(n, cache=[0, 1]):
#     if len(cache) < n + 1:
#         cache.append(fib(n - 1, cache) + fib(n - 2, cache))
#     return cache[n]

# from functools import cache

# @cache
# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     return fib(n - 1) + fib(n - 2)

# print(fib(50))
    

# class Vector3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     @classmethod
#     def init_from_list(cls, data):
#         x, y, z = data
#         return cls(x, y, z)

#     @staticmethod
#     def dot_product(first, second):
#         return first.x * second.x + first.y * second.y + first.z * second.z
    
    

# a = Vector3D(3, 5, 4)
# b = Vector3D(0, 6, 2)
# print(Vector3D.dot_product(b, a))
# c = Vector3D.init_from_list([8, 1, 1])
# print(c.x, c.y, c.z, c)


# class Basic:
#     def __init__(self, x):
#         self._x = x

#     @property
#     def x(self):
#         return self._x
    
    # @x.setter
    # def x(self, value):
    #     if isinstance(value, int):
    #         self._x = value
    #     else:
    #         raise ValueError
        

# A = Basic(3)

# A.set_x("oidwvnoin")
# A.set_x(5)
# print(A.get_x())

# A.x = 5
# print(A.x)
# A.x = "wieo"

class Base:
    def func(self):
        pass

class Derived(Base):
    pass

x = Derived()
x.func()
print(Derived.__dict__)
print(Base.__dict__)