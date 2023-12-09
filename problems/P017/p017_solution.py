def P017(number):
    m = []
    d = '+'
    e = '0'
    for c in range(0 , number + 1):
        f = number - c
        m.append(d * c + e * f)
    return m
if __name__ == "__main__":
    a = int(input())
    answer = P017(a)
    for f in answer:
        print(f)