n = int(input())

unpure_symptoms = (",", ".", "_")

for _ in range(n):
    string = input()
    is_pure = True
    for char in string:
        if char in unpure_symptoms:
            is_pure = False
            
    if is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")