class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.__counted = -1

    def __iter__(self):
        return self
        
    def __next__(self):
        self.__counted += 1
        if self.__counted == self.count:
            raise StopIteration
        return self.__counted * self.step

#------------- Test code -------------#

numbers = take_skip(100, 10)
for number in numbers:
    print(number)