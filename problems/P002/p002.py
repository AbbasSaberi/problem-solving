def c(number_1 , number_2):
    return(number_1 + number_2)
def d(number_1 , number_2):
    return(number_1 - number_2)
def e(number_1 , number_2):
    return(number_1 * number_2)
def f(number_1  , number_2):
    return(number_1 / number_2)
def function(number_1 , number_2):
    return c(number_1 , number_2) , d(number_1 , number_2), e(number_1 , number_2) , int(f(number_1 , number_2))
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    answer = function(a , b)
    print(answer)