def figunahe(number):
    m = []
    m.append(1)
    m.append(1)
    a = 1
    b = 1
    for c in range(0 , number):
        a = a + b
        b = a + b
        if a < number:
            if b < number:
                m.append(a)
                m.append(b)
    return m

if __name__ == '__main__':
    input = int(input())
    answer = figunahe(input)
    print(answer)