import weakref
import gc

class MyObject(object):
    idx = 0
    def __init__(self) -> None:
        MyObject.idx += 1

    def idxInc(self):
        self.idx+=1

    def my_method(self):
        print ('my_method was called!')


obj = MyObject()
print(obj.idx)

obj1 = MyObject()
print(obj.idx)

r = weakref.ref(obj)
print(obj.idx)

gc.collect()
assert r() is obj #r() allows you to access the object referenced: it's there.
print(obj.idx)

obj = 1 #Let's change what obj references to
gc.collect()
assert r() is None
