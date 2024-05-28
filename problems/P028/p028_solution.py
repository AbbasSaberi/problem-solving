INPUT = int(input('number of inputs : '))
m = []
for x in range(1, INPUT + 1):
    Input = input(f'input{x} : ').split(' ')
    m.append(Input)
list = {}
for s in m:
    l = s[0]
    L = s[1]
    list.update({l : L})

point = input('points : ').split(' ')
list_X = []
list_Y = []
list_print = []
T = 1
x = 1
y = 1
for X in range(len(point)):
    member_X = int(list[point[X]][0])
    member_Y = int(list[point[X]][int(len(list[point[X]]) - 1)])
    list_X.append(member_X)
    list_Y.append(member_Y)
    if X >= 1 :
        T += 1
        output_X = 0
        output_Y = 0
        output_X = abs(list_X[x - 1] - list_X[x])
        x += 1
        output_Y = abs(list_Y[y - 1] - list_Y[y])
        y += 1
        output = output_X + output_Y
        list_print.append(output)
OUTPUT = 0
for sumlist in list_print:
    OUTPUT = OUTPUT + sumlist
print(OUTPUT)