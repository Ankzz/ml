# This file implements a Class specific private variable 
# A private class variable can be declared by adding __ (double underscore) as prefix to the variable name
#
# Details:
# Class A has a private variable __b
# __b cannot be directly accessed using class A object. But can be accessed via its mangled name.
#
# @author: Ankit <da25m546@smail.iitm.ac.in>; Ankit <ankzzdev@gmail.com>
class A:
    # _a:any
    # __b:any
    def __init__(self):
        self._a = 0
        self.__b = "A private item"
        pass


if __name__ == "__main__":
    obj = A()
    print(obj._a) ## Will print the value assigned to _a
    try:
        print(obj.__b) ## Leads to error: 'A' object has no attribute '__b'
    except:
        print(obj._A__b) ## '__' or private variable is name mangled in Python. 
                         ## It is stored as _<ClassName>__<VariableName>
                         ## In this case __b is stored under A as _A__b
        pass

    print(hasattr(obj, "__b")) # Prints: False
    print(hasattr(obj, "_A__b")) # Prints: True

    pass