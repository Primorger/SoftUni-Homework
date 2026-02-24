def craft_presents(materials_input, magic_input):
    materials = [int(x) for x in materials_input.split()]
    magic = [int(x) for x in magic_input.split()]
    
    toys = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
    crafted = {}
    
    while materials and magic:
        mat = materials[-1]
        mag = magic[0]
        
        if mat == 0 and mag == 0:
            materials.pop()
            magic.pop(0)
            continue
        elif mat == 0:
            materials.pop()
            continue
        elif mag == 0:
            magic.pop(0)
            continue
        
        product = mat * mag
        
        if product in toys:
            toy_name = toys[product]
            crafted[toy_name] = crafted.get(toy_name, 0) + 1
            materials.pop()
            magic.pop(0)
        elif product < 0:
            total = mat + mag
            materials.pop()
            magic.pop(0)
            materials.append(total)
        else:
            magic.pop(0)
            materials[-1] += 15
    
    doll_train = "Doll" in crafted and "Wooden train" in crafted
    bear_bicycle = "Teddy bear" in crafted and "Bicycle" in crafted
    
    if doll_train or bear_bicycle:
        print("The presents are crafted! Merry Christmas!")
    else:
        print("No presents this Christmas!")
    
    if materials:
        print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
    
    if magic:
        print(f"Magic left: {', '.join(map(str, magic))}")
    
    for toy in sorted(crafted.keys()):
        print(f"{toy}: {crafted[toy]}")


materials_input = input()
magic_input = input()
craft_presents(materials_input, magic_input)