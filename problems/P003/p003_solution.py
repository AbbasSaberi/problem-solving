def Year(number_1 , number_2):
    c = number_1 - number_2
    d = abs(c)
    return d * 365
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    answer = Year(a , b)
    print()
    print(answer,'Dey')