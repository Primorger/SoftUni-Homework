def make_honey(bees_input, nectar_input, symbols_input):
    bees = [int(x) for x in bees_input.split()]
    nectar = [int(x) for x in nectar_input.split()]
    symbols = symbols_input.split()
    
    total_honey = 0
    
    while bees and nectar:
        bee = bees[0]
        nec = nectar[-1]
        
        if nec >= bee:
            symbol = symbols.pop(0)
            
            if symbol == "/" and nec == 0:
                bees.pop(0)
                nectar.pop()
                continue
            
            if symbol == "+":
                result = bee + nec
            elif symbol == "-":
                result = bee - nec
            elif symbol == "*":
                result = bee * nec
            elif symbol == "/":
                result = bee / nec
            
            total_honey += abs(result)
            bees.pop(0)
            nectar.pop()
        else:
            nectar.pop()
    
    print(f"Total honey made: {total_honey}")
    
    if bees:
        print(f"Bees left: {', '.join(map(str, bees))}")
    
    if nectar:
        print(f"Nectar left: {', '.join(map(str, nectar))}")


bees_input = input()
nectar_input = input()
symbols_input = input()
make_honey(bees_input, nectar_input, symbols_input)