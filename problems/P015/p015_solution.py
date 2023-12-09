def P015(number_1 , number_2):
    def sumlist(number_2):
        d = 0
        for c in number_2:
            d = d + c
        return d
    return sumlist(number_2)
if __name__ == "__main__":
    m = []
    a = int(input('int : '))
    for c in range(0 , a):
        b = int(input(f'input {c + 1} : '))
        m.append(b)
    answer = P015(a , m)
    print(answer)