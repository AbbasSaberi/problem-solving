def P006(number):
    A = (((number + 1) * number) / 2)
    return A

if __name__ == '__main__':
    a = int(input())
    answer = P006(a)
    print(answer)