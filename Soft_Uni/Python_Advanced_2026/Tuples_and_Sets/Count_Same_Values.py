nums = tuple([float(x) for x in input().split()])

data = {}

for element in nums:
    if element not in data:
        data[element] = nums.count(element)

for element, count in data.items():
    print(f"{element:.1f} - {count} times")