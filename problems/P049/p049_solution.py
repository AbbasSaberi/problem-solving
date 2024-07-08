INPUT = int(input('number of inputs: '))
m = []
for x in range(INPUT):
    a = input(f'input{x + 1}: ').split(' ')
    m.append(a)
Point = input('Point: ').split(' ')
b = input('Name of the planet: ')
point1 = 0
point2 = 0
for x in range(INPUT):
    if m[x][0] == b:
        point1 = int(m[x][1]) - int(Point[0])
        point2 = int(m[x][2]) - int(Point[1])
output = ((point1 ** 2) + (point2 ** 2)) ** 0.5
print(output)