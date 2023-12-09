def is_preme(number):
    m = []
    for d in range(2 , number):
        ispreme = True
        for c in range(2 , d):
            if d % c == 0:
                ispreme = False
        if ispreme:
            m.append(d)
    return m
if __name__ == '__main__':
    a = int(input())
    answer = is_preme(a)
    print(answer)