import random
# import sys
# class trash:
#     def __init__(self):
#         print("I got some 回收垃圾")
    
#     def __del__(self):
#         print("这是真的垃圾，不能回收")

#     def needntrecycle(self):
#         print("浪费垃圾")

# garb = trash()
# garb.needntrecycle()
# print(sys.getsizeof(garb))
# del garb

# garb2 = trash()
# garb2.needntrecycle()
# print("omagod")


class sq_area_calc:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def intro(self):
        print("I'm a rectangle i guess")
    def area(self):
        print("I'm boring and my area is: " + str(self.x * self.y))
    
class tr_area_calc:
    def __init__(self,ps1,ps2,h):
        self.ps1 = ps1
        self.ps2 = ps2
        self.h = h

    def intro(self):
        print("早上好中国！ 现在我有冰淇淋！")
    
    def area(self):
        print("I'm much cooler and better than rectangle i got an area of: " + str((self.ps1 + self.ps2)*self.h/2))

rando = random.randint(2,3)
if rando == 2:
    x = random.randint(1,10)
    y = random.randint(1,10)
    objec = sq_area_calc(x,y)
else:
    x = random.randint(1,10)
    y = random.randint(1,10)
    z = random.randint(1,10)
    objec = tr_area_calc(x,y,z)
objec.area()
