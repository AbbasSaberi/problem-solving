def P018(number):
    m = []
    def is_preme(number):
        ispreme = True
        for d in range(2 , number):
            if number % d == 0:
                ispreme = False
                break
            return ispreme
    for c in range(2 , number):
        if is_preme(c) and is_preme(c + 2):
            m.append((c , c + 2))
    return m
if __name__ == "__main__":
    a = int(input())
    answer = P018(a)
    for c in answer:
        print(c)