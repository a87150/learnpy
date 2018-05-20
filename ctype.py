import ctypes 
a = 1 
print(a, id(a)) 

def deref(addr, typ): 
    return ctypes.cast(addr, ctypes.POINTER(typ)) 

deref(id(1), ctypes.c_int)[6] = 100

print (a, id(a)) 