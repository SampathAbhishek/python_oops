#multiple inheritance(OOPS CONCEPT ----in PYTHON)
class A:
    def __init__(self):
        print("init function of A")
    def feature1(self):
        print("feature 1 printing...")
    def feature2(self):
        print("feature 2 printing...")

class B():
    def __init__(self):
        print("init function of B")
    def feature3(self):
        print("feature 3 printing...")
    def feature4(self):
        print("feature 4 printing...")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("init function of C")
    def feature5(self):
        print("feature 5 printing...")
    def feature6(self):
        print("feature 6 printing...")

#why only init function of a is being called but c has two parents a and b?
# ans: This is because of the concept of method resolution Order in python.
# it takes only in the parents order of left to right.(A->B) a is first so it took a

obj_c = C()
obj_c.feature1()
obj_c.feature2()
obj_c.feature3()
obj_c.feature4()
obj_c.feature5()
obj_c.feature6()
