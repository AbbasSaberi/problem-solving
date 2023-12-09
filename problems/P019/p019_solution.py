def P019(number):
    ouput = []
    a = [1]
    b = [1 , 1]
    if len(a) <= number:
        ouput.append(a)
    if len(b) <= number:
        ouput.append(b)
    while len(a) <= number and len(b) <= number:
        a = [1]
        if len(b) <= number:
            x = 0
            y = 1
            while y < len(b):
                a.append(b[x] + b[y])
                x += 1 
                y += 1
            a.append(1)
            if len(a) <= number :
                ouput.append(a)
        if len(a) <= number:
            b = [1]
            x = 0
            y = 1
            while y < len(a):
                b.append(a[x] + a[y])
                x += 1
                y += 1
            b.append(1)
            if len(b) <= number:
                ouput.append(b)
    return ouput
if __name__ == "__main__":
    INPUT = int(input('int : '))
    answer = P019(INPUT)
    for IXI in answer:
        print(IXI)