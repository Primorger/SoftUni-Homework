from string import punctuation

with open("Exercise_File_Handling\\Line_Numbers\\text.txt") as input_file, open("Exercise_File_Handling\\Line_Numbers\\output.txt", "w") as output_file:
    result = []
    for i, line in enumerate(input_file):
        char_count = 0
        special_symbol_count = 0
        for char in line:
            if char.isalpha():
                char_count += 1
            elif char in punctuation:
                special_symbol_count += 1

        result.append(f"Line {i + 1}: {line.strip()} ({char_count})({special_symbol_count})")
    output_file.write("\n".join(result))