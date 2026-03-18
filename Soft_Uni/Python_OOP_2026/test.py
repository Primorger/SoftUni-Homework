class Classic:
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def create_john(cls):
        return cls("John")
    
    @staticmethod
    def add(a, b):
        return a + b
    
print(Classic.create_john())
print(Classic.add(10, 56))