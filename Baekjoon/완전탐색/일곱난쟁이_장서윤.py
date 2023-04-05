cm = 0
dwarf = list()
loop = True

for i in range(9):
    dwarf.append(int(input()))
    cm += dwarf[len(dwarf)-1]

for idx1 in range(8):
    for idx2 in range(idx1+1, 9):
        if cm - 100 == dwarf[idx1] + dwarf[idx2]:
            del dwarf[idx2]
            del dwarf[idx1]
            loop = False
            break
    if not loop:
        break

dwarf.sort()

for i in dwarf:
    print(i)