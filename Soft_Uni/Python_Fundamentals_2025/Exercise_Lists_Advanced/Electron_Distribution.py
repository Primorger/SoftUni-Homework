number_of_electrons = int(input())
electron_shell = [0]
electron_ring = 1

for electron in range(number_of_electrons):
    electron_shell[electron_ring - 1] += 1
    if electron_shell[electron_ring - 1] ==  2 * (electron_ring**2):
        electron_ring += 1
        electron_shell.append(0)

if 0 in electron_shell:
    electron_shell.remove(0)
print(electron_shell)