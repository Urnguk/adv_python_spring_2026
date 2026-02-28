# class A:
#     x = 10

# a = A()
# b = A()

# print(a.x, b.x)
# a.x = 13
# print(a.__dict__)
# print(b.__dict__)
# A.x = 5
# print(a.x, b.x)

# ----------------------------------------

# class A:
#     X = []

# a = A()
# b = A()

# a.X.append(1)

# print(A.__dict__)

# ----------------------------------------

# class Student:
#     def __init__(self, name, age, group):
#         self.group = group
#         self.name = name
#         self.age = age
#         self.stypend = True
#         self.currency = 0
    
#     def pay(self):
#         if self.stypend:
#             self.currency += 5600

# x = Student("Леха", 20, "Б06-301")

# print(x.__dict__)
# print(Student.__dict__)

# # y = Student()
# # print(y.name)

# x.pay()
# x.pay()
# print(x.currency)

# ----------------------------------

# class AccountedClass:
#     cnt = 0

#     def __init__(self):
#         AccountedClass.cnt += 1
    
# a = AccountedClass()
# b = AccountedClass()

# print(a.cnt)

# c = AccountedClass()
# print(a.cnt)

# -------------------------------------------

# class X:
#     def __init__(self):
#         self.a = 0
#         self.__b = 0
    
#     def func(self):
#         self.a += 1
#         self.__b += 1
    
#     def get(self):
#         return self.a, self.__b
    
# x = X()
# print(x.a)
# x.func()
# print(x.get())

# x.__dict__["_X__b"] = 3
# print(x.get())

# ----------------------------------------

# class X:
#     def __init__(self):
#         self.a = 0
#         self._b = 0
    
#     def func(self):
#         self.a += 1
#         self._b += 1
    
#     def get(self):
#         return self.a, self._b
    
# x = X()
# print(x.a)
# print(x._b)

# ---------------------------------

# class X:
#     def __len__(self):
#         return 3

    
# x = X()
# print(len(x))


# ---------------------------------

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, 
                            self.y + other.y, 
                            self.z + other.z)
        else:
            return Vector3D(self.x + other, 
                            self.y + other, 
                            self.z + other)
    
    def __str__(self):
        return f"Vector3D at x = {self.x}, y = {self.y}, z = {self.z}"


a = Vector3D(3, 5, 7)
b = Vector3D(0, 4, -2)
print(a + b)
print(b + 1)
print(1 + b)

