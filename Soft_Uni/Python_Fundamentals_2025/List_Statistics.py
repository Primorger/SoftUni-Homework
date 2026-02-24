lst_positive = []
lst_negative = []

length = int(input())

for _ in range(length):
    obj = int(input())

    if obj > 0:
        lst_positive.append(obj)
    else:
        lst_negative.append(obj)
    
print(lst_positive)
print(lst_negative)


print(f"Count of positives: {len(lst_positive)}\nSum of negatives: {sum(lst_negative)}")