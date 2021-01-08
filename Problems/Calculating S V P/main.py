a = int(input())
b = int(input())
c = int(input())

length_of_edges = 4 * (a + b + c)
surface_area = 2 * (a * b + b * c + a * c)
volume = a * b * c

print(length_of_edges)
print(surface_area)
print(volume)