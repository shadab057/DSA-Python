# ctypes - A foreign function library for Python. 
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries. 
# It can be used to wrap these libraries in pure Python.

import ctypes
class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type array with size = self.size 1
        self.A = self.__make_array(self.size)
    
    def __make_array(self, new_size):
        return (new_size * ctypes.py_object)()  # create array of size new_size
    
L = MeraList()
print(type(L))