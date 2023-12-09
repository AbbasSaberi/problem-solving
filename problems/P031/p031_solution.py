def P031(number):
    n = []
    if number < 2:
        return f"{number} < 2"
    else:
        m = []
        for b in range(2 , number):
            is_preme = True
            for d in range(2 , b):
                if b % d ==0:
                    is_preme = False
            if is_preme:
                m.append(b)
    for X in range(len(m)):
        for Y in range(1 , len(m)):
            if m[X] + m[Y] == number:
                if number % 2 ==0:
                    n.append((m[X] , m[Y]))
                if number % 2 !=0:
                    n.append((f"{number} is odd"))
    return n
if __name__ == "__main__":
    a = int(input("int : "))
    answer = P031(a)
    for b in answer:
        print(b)