def P047(number):
    m = []
    for b in range(2 , number):
        ispreme = True
        for c in range(2 , b):
            if b % c == 0:
                ispreme = False
        if ispreme:
            m.append(b)
    return len(m)
if __name__ == "__main__":
    a = int(input("int : "))
    answer = P047(a)
    print(answer)