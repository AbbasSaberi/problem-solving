def written_number(number):
    if number == 1:
        return 'one'
    if number == 2:
        return 'two'
    if number == 3:
        return 'three'
    if number == 4:
        return 'four'
    if number == 5:
        return 'five'
    if number == 6:
        return 'six'
    if number == 7:
        return 'seven'
    if number == 8:
        return 'eight'
    if number == 9:
        return 'nine'
    if number == 10:
        return 'ten'

if __name__ == '__main__':
    a = int(input())
    answer = written_number(a)
    print(answer) 