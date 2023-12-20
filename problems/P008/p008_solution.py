def P008(number):
    for c in range(1 , number):
        number = number * c
    return number

if __name__ == '__main__':
    a = int(input('number : '))
    answer = P008(a)
    print(answer)