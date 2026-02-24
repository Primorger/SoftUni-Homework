sequence_1 = set([int(x) for x in input().split()])
sequence_2 = set([int(y) for y in input().split()])

n = int(input())

for _ in range(n):
    command = input().split()
    action = command[:2]
    seq_of_nums = set([int(command[i]) for i in range(2, len(command))])

    if action[0] == "Add":
        if action[1] == "First":
            sequence_1 = sequence_1.union(seq_of_nums)

        elif action[1] == "Second":
            sequence_2 = sequence_2.union(seq_of_nums)

    elif action[0] == "Remove":
        if action[1] == "First":
            sequence_1 = sequence_1.difference(seq_of_nums)

        elif action[1] == "Second":
            sequence_2 = sequence_2.difference(seq_of_nums)

    elif action[0] == "Check":
        print(sequence_1.issubset(sequence_2) or sequence_2.issubset(sequence_1))

sequence_1_as_str = [str(el) for el in sorted(sequence_1)]
sequence_2_as_str = [str(el) for el in sorted(sequence_2)]

print(", ".join(sequence_1_as_str))
print(", ".join(sequence_2_as_str))