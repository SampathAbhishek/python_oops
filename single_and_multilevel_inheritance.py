class A:
    def __init__(self):
        print("init function of A")
    def feature1(self):
        print("feature 1 printing...")
    def feature2(self):
        print("feature 2 printing...")

class B(A):
    def __init__(self):
        super().__init__()
        print("init function of B")
    def feature3(self):
        print("feature 3 printing...")
    def feature4(self):
        print("feature 4 printing...")

class C(B):
    def __init__(self):
        super().__init__()
        print("init function of C")
    def feature5(self):
        print("feature 5 printing...")
    def feature6(self):
        print("feature 6 printing...")

obj_c = C()
obj_c.feature1()
obj_c.feature2()
obj_c.feature3()
obj_c.feature4()
obj_c.feature5()
obj_c.feature6()
