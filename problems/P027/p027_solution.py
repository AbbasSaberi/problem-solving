a = input("input : ")
if a[0:3] == 'P: ':
    m = []
    x1 = 3
    x2 = 3
    for x in range(3 , len(a)):
        if a[x2] == ' ':
            m.append(a[x1:x2])
            x1 = x2 + 1
        if a[x2] == '.':
            m.append(a[x1:(x2 + 1)])
            x1 = x2 + 1
        x2 += 1
    w = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
    n = []
    x = 1
    X1 = 0
    X2 = 1
    for A in m:
        P = ''
        x3 = 0
        while x3 != len(n):
            X1 = 0
            X2 = 1
            for p in range(len(n)):
                p1 = n[X1]
                P1 = p1[1]
                x3 += 1
                if len(n) != 1:
                    p2 = n[X2]
                    P2 = p2[1]
                    X1 += 1
                    if len(n) - 1 != X1:
                        X2 += 1
                    if A == P2:
                        P = P2
        if A != P:
            if A == m[0]:
                n.append((w[x],A))
                x += 1
            if A != m[0]:
                n.append((w[x],A))
                x += 1
    i = []
    for v in m:
        for V in range(len(n)):
            p1 = n[V]
            P1 = p1[1]
            if v == P1:
                i.append((P1,w[V + 1]))
    I = []
    for OUTPUT in i:
        Print = OUTPUT[1]
        I.append(Print)
    print(str(" ".join(I)))
    for output in n:
        print(str(" ".join(output)))
if a[0:3] == 'E: ':
    m = [a[3:len(a)]]
    n = []
    A = 1
    while True:
        b = input(f'input {A} : ')
        A += 1
        if b == 'END':
            break
        n.append(b)
    output = []
    v = m[0]
    for x in range(len(v)):
        if v[x] != ' ':
            for X in n:
                if X[0] == v[x]:
                    output.append(X[2:len(X)])
    print(str(" ".join(output)))