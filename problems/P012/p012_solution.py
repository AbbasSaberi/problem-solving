def prime_number(number):
    m = []
    A = 1
    x = 0
    while x < number:
        A = A + 1
        ispreme = True
        for B in range(2 , A):
            if A % B ==0:
                ispreme = False
        if ispreme:
            m.append(A)
            x = x + 1
    return m[x - 1]
if __name__ == '__main__':
    a = int(input())
    answer = prime_number(a)
    print(answer)