def is_prime(func):
    def wrapper(*args):
        summa = func(*args)
        for i in range(2, summa):
            if summa % i == 0:
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime == True:
            return (f'Простое \n{summa}')
        else:
            return (f'Составное \n{summa}')
    return wrapper
@ is_prime
def sum_three(*value):
    summa = sum(value)
    return summa

result = sum_three(2, 3, 6)
print(result)
