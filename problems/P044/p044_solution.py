a = input('numbers : ').split()
m = []
A = 1
while True:
    b = input(f'number{A} : ')
    A += 1
    m.append(b)
    if b == 'END':
        break
n = []
for X in m:
    for x1 in a:
        for x2 in a:
            if X != 'END':
                if int(x1) + int(x2) == int(X):
                    n.append(f'{int(X)} = {int(x1)} + {int(x2)}')
                    if len(m) - 1 != len(n):
                        for X in m:
                            for x1 in a:
                                for x2 in a:
                                    for x3 in a:
                                        if X != 'END':
                                            if int(x1) + int(x2) + int(x3) == int(X):
                                                n.append(f' {int(X)} = {int(x1)} + {int(x2)} + {int(x3)} ')

for ouput in n:
    print(ouput)