atoms_before = int(input())
atoms_after = int(input())

check = atoms_before
half_life = 0

while check >= atoms_after:
    check /= 2
    half_life += 1

decay = half_life * 12

print(decay)