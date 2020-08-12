class WithoutSlots:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class WithSlots:
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def instance_fn(cls):
    def instance():
        x = cls(1, 2, 3)
    return instance

print(instance_fn(WithoutSlots(1,2,3)))