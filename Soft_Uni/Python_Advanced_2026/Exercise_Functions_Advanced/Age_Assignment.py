def age_assignment(*args, **kwargs):
    result = []
    
    for name in args:
        first_letter = name[0]
        age = kwargs[first_letter]
        result.append((name, age))
    
    result.sort(key=lambda x: x[0])
    
    output = []
    for name, age in result:
        output.append(f"{name} is {age} years old.")
    
    return "\n".join(output)