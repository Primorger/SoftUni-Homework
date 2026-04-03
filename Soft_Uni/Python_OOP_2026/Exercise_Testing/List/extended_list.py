class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)
    
from unittest import TestCase, main

class IntegerListTests(TestCase):
    def test_init(self):
        i = IntegerList(1, 2, 4, 5, "Hello, there")
        self.assertEqual(i.get_data(), [1, 2, 4, 5])
    
    def test_add_exception(self):
        i = IntegerList(1, 2, 4, 5, "Hello, there")
        with self.assertRaises(Exception) as ex:
                i.add("animal")
        self.assertEqual("Element is not Integer", str(ex.exception))
        
    def test_add(self):
        i = IntegerList(1, 2, 4, 5, "Hello, there")
        
        result = i.add(3)
    
        self.assertEqual(result, [1, 2, 4, 5, 3])    
        
    def test_remove_index(self):
        pass    
        
        
if __name__ == "__main__":
    main()