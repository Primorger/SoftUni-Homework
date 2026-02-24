number_list = list(map(int, input().split(", ")))
even_indicies = [i for i in range(len(number_list)) if number_list[i] % 2 == 0]
print(even_indicies)