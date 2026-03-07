# class Base:
#     def __str__(self):
#         return "this is base class"
    
#     def move(self):
#         print('I have moved')


# class Derived(Base):
#     def __str__(self):
#         return "this is derived class"

# x = Derived()
# x.move()
# print(x)


# class Tree:
#     def __init__(self, type="Tree"):
#         self.type = type
#         self.roots = 1
#         self.name = 'Tree'
    
#     def __str__(self):
#         return f"This is {self.type} named {self.name} with roots length {self.roots}"
    
# class Birch(Tree):
#     def __init__(self, type="Birch"):
#         super().__init__(type)
#         self.leaves = 10 ** 9

#     def __str__(self):
#         return super().__str__() + f" and leaves in amount {self.leaves}"

# x = Birch()
# print(x)


# print(1 / 0)
# A = []
# print(A[5])
# int("dsivo")
# 3 + "abc"
    # print(1)


# raise ZeroDivisionError

# try:
#     raise ValueError
# except ArithmeticError:
#     print("don't divide by zero")
# else:
#     print("no errors")
# finally:
#     print("will always work")

# class MyError(Exception):
#     pass

# raise MyError

# try:
#     f = open("tmp.txt")

# finally:
#     f.close()

# with open("C:\\Users\\Urnguk\\Documents\\Programming\\Python\\MIPT\\adv_python_spring_2026\\Lesson_4\\tmp.txt", mode="tx") as file:
#     # print(file.readline().strip())
#     # print(file.readline())
#     for line in file:
#         print(line.strip())

import pickle

# D = {1:3, 2:6}
# with open("tmp.bin", mode="wb") as file:
#     pickle.dump(D, file)

with open("tmp.bin", mode="rb") as file:
    X = pickle.load(file)

print(X)