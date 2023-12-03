def P005(number_1 , number_2 , number_3):
    if number_2 == '+':
        return number_1 + number_3
    if number_2 == '-':
        return number_1 - number_3
    if number_2 == '*':
        return number_1 * number_3
    if number_2 == '/':
        return number_1 / number_3
if __name__ == "__main__":
    a = int(input())
    b = input()
    c = int(input())
    answer = P005(a , b , c)
    print()
    print(answer)