def is_prime(num: int):
    if num <= 1:
        return False
    else:
        for i in range(2,num):
            if (num % i) == 0:
                return False
    return True


def print_primes(count: int):
    num: int = 0
    i = 0
    while i < count:
        num += 1
        if is_prime(num):
            print(num)
            i += 1


print_primes(10)
