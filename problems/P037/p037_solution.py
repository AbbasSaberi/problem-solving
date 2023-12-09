def P037(number_1 , number_2):
    for x1 in number_1:
        for x2 in number_2:
            if x1 == x2:
                number_1.remove(x1)
            if x1.endswith('.'):
                if x1 == x2 + '.':
                    number_1.insert(number_1.index(x1) , '.')
                    number_1.remove(x1)
            if x1.endswith(','):
                if x1 == x2 + ',':
                    number_1.insert(number_1.index(x1) , ',')
                    number_1.remove(x1)
            if x1.endswith('!'):
                if x1 == x2 + '!':
                    number_1.insert(number_1.index(x1) , '!')
                    number_1.remove(x1)
            if x1.endswith('?'):
                if x1 == x2 + '?':
                    number_1.insert(number_1.index(x1) , '?')
                    number_1.remove(x1)
    return str(" ".join(number_1))
if __name__ == "__main__":
    a = input("input : ").split(' ')
    m = []
    A = 1
    while True:
        b = input(f"input {A} : ")
        if b == 'END':
            break
        m.append(b)
        A += 1
    answer = P037(a , m)
    print(answer)