def P039(number_1, list_1):
    m = []
    for w in range(len(list_1)):
        for x in list_1[w]:
            I = 0
            for W in range(len(list_1)):
                for X in set(list_1[W]):
                    if x == X:
                        I += 1
                        if I == number_1:
                            u = list(map(lambda f: f[0] , m))
                            if x not in u:
                                m.append((x , I))
    m.sort(key=lambda p: -1 * p[1])
    m.reverse()
    ouput = []
    for OUPUT in m:
        ouput.append(OUPUT[0])
    return " ".join(ouput)

if __name__ == '__main__':
    a = int(input('int : '))
    n = []
    for A in range(1 , a + 1):
        b = input(f'list {A} : ')
        n.append(b.split())
    answer = P039(a , n)
    print(answer)    