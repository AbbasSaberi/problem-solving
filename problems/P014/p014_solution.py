def P014(number_1 , number_2 , NUMBER_1 , NUMBER_2):
    def merge (number_2 , NUMBER_2):
        return number_2 + NUMBER_2
    return merge(number_2 , NUMBER_2)
if __name__ == "__main__":
    m = []
    a = int(input('int(m) : '))
    for c in range(0 , a):
        b = input(f"input {c + 1}(m) : ")
        m.append(b)
    n = []
    A = int(input('int(n) : '))
    for e in range(0 , A):
        B = input(f"input {e + 1}(n) : ")
        n.append(B)
    answer = P014(a , m , A , n)
    print(answer)