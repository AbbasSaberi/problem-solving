def P013(number):
    def prime_list(number):
        m = []
        for d in range(2 , number):
            ispreme = True
            for c in range(2 , d):
                if d % c ==0:
                    ispreme = False
            if ispreme:
                m.append(d)
        return m
    b = prime_list(number)
    output = []
    for shirpharhad in b:
        while number % shirpharhad ==0:
            number = number / shirpharhad
            output.append(shirpharhad)
    return output
if __name__ == '__main__':
    a = int(input())
    answer = P013(a)
    print(answer)