a = int(input())
print('input')
m = []
ouput = []
for A in range(1 , a + 1):
    d = int(input())
    m.append(d)
print('ASC or DESC')
b = input()
H = 0
for I in m:
    H = H + I
if b == 'ASC':
    for x in range(1 , H):
        for p in range(1 , a + 1):
            y = m[p - 1]
            if y == x:
                ouput.append(y)
if b == 'DESC':
    for X in range(H , 0 , -1):
        for P in range(a , 0 , -1):
            Y = m[P - 2]
            if Y == X:
                ouput.append(Y)
print(ouput)