def primorial(number):
    m = []
    for d in range(2 , number):
        ispreme = True
        for e in range(2 , d):
            if d % e == 0:
                ispreme = False
        if ispreme:
            m.append(d)
    def beat(m):
        b = 1
        for c in m:
            b = b * c
        return(b)
    return beat(m)

if __name__ == '__main__':
    a = int(input())
    answer = primorial(a)
    print(answer)