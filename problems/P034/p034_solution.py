def P034(number):
    n = []
    m = []
    x1 = -1
    A = 0
    while A != len(str(number)):
        x2 = 1
        m.append(str(number)[x1])
        x1 += 1
        A += 1
        while True:
            if x2 >= len(str(number)):
                break
            x2 += 1
            if x1 != x2:
                if str(number)[x1:x2] != '':
                    m.append(str(number)[x1:x2])
    for b in m:
        if int(b) != 1:
            if int(b) not in n:
                is_preme = True
                for d in range(2 , int(b)):
                    if int(b) % d ==0:
                        is_preme = False
                if is_preme:
                        n.append(int(b))
    return n
if __name__ == "__main__":
    a = int(input("int : "))
    answer = P034(a)
    for b in answer:
        print(b)