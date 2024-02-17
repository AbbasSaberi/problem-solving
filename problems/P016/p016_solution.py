def solution(number):
    m = []
    d = '@'
    for b in range(number , 0 , -1):
        m.append(d * b)
    return m
if __name__ == '__main__':
    a = int(input("Enter the number: "))
    answer = solution(a)
    for b in answer:
        print(b)