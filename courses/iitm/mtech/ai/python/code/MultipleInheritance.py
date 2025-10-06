# This file implements multiple inheritance - a special case of a common method
#
# Details:
# In this example A and B are parent class which expose the method "name"
# Class C inherits A and B both.
# When object of class C calls method name - method of parent class gets executed
# Method called depends on order of inheritance - first method in that list
#
# @author: Ankit <da25m546@smail.iitm.ac.in>; Ankit <ankzzdev@gmail.com>
#
class A:
    def name(self):
        return "A"
    
class B:
    def name(self):
        return "B"
    
class C(A, B):
    pass

class D(B, A):
    pass

if __name__ == "__main__":
    obj = C()
    print(obj.name()) # Calls name of class A

    obj = D()
    print(obj.name()) # Calls name of class B