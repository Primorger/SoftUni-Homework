class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx_in_seq = -1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.idx_in_seq += 1
        self.count += 1
        if self.idx_in_seq == len(self.sequence):
            self.idx_in_seq = 0
        if self.count > self.number:
            raise StopIteration
        return self.sequence[self.idx_in_seq]

#------------- Test code -------------#

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')