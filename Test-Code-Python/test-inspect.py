import traceback

class A():
    def aa(self):
        print('aa')
    def ba(self):
        print('ba')

class B(A):
    def ab(self):
        traceback.print_stack()
        print('ab')
    def bb(self):
        print('bb')

b = B()
b.ab()