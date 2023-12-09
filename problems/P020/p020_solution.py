def P020(number):
    b = {1 : 'one',2 : 'twu', 3 : 'three',4 : 'four',5 : 'five',6 : 'six',7 : 'seven',8 : 'eight',9 : 'nine',10 : 'ten'}
    if 10 >= number:
        return f"{number} is {b[number]}"
    else:
        return f"{number} not found"
if __name__ == "__main__":
    a = int(input('int from 1 to 10 : '))
    answer = P020(a)
    print(answer)