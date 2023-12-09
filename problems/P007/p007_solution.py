def P007(list):
    m = []
    for x in range(1 , list + 1):
        if x % 5 ==0:
          m.append(x)
    return m  

if __name__ == '__main__':
    a = int(input())
    answer = P007(a)
    print(answer)