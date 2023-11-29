def even_odd(number):
    if number % 2 == 0:
        return(f'{number} is even')
    else : 
        return(f'{number} is odd')

if __name__ == '__main__':
    a = int(input())
    answer = even_odd(a)
    print(answer)