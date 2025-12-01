import ctypes

class MeraList:
    def __init__(self):
        self.size = 1        # List ki max capacity
        self.n = 0           # Abhi kitne items hain
        self.A = self.__make_array(self.size)
    
    def __len__(self):
        return self.n
    
    # Print karne ke liye
    def __str__(self):
        # [1,2,3,4]
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'

    def append(self, item):
        # Agar list full ho gayi hai, toh size double karo
        if self.n == self.size:
            self.resize(self.size * 2)
        
        # Item ko insert karo
        self.A[self.n] = item
        self.n = self.n + 1
    
    def resize(self, new_capacity):
        # 1. Naya array banao
        B = self.__make_array(new_capacity)
        
        # 2. Purane elements copy karo
        for i in range(self.n):
            B[i] = self.A[i]
            
        # 3. Purane array ko replace karo
        self.A = B
        
        # 4. CRITICAL STEP: Size variable ko update karo!
        self.size = new_capacity  
        
    def __make_array(self, capacity):
        # Ctypes array create karta hai
        return (capacity * ctypes.py_object)()

# Testing
L = MeraList()
L.append(10)
L.append(3.4)
L.append(True)
L.append('Hello World')
# print("Code successfully chal gaya!")
print(L)