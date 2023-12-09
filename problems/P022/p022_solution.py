def P022(number , number_1 , number_2):
    output = []
    for x in range(1 , number + 1):
        A = int(number_1[x - 1]) + int(number_2[x - 1])
        output.append(str(A))
    print()
    return " ".join(output)
if __name__ == "__main__":
    a = int(input())
    b = input().split(' ')
    B = input().split(' ')
    answer = P022(a , b , B)
    print(answer)