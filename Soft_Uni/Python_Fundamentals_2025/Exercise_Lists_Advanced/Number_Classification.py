numbers = list(map(int, input().split(", ")))
positives = []
negatives = []
even = []
odd = []
def is_positive(num):
    if num >= 0:
        return True
def is_even(num):
    if num % 2 == 0:
        return True
    
for number in numbers:
    if is_positive(number):
        positives.append(str(number))
    else:
        negatives.append(str(number))
    if is_even(number):
        even.append(str(number))
    else:
        odd.append(str(number))
        
print(f"Positive:", ", ".join(positives))
print(f"Negative:", ", ".join(negatives))
print(f"Even:", ", ".join(even))
print(f"Odd:", ", ".join(odd))