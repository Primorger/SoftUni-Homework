class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.__curr_num = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.__curr_num -= 1
        if self.__curr_num < 0:
            raise StopIteration
        return self.__curr_num
    
#------------- Test code -------------#

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")