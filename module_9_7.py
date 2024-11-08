def is_prime(func):
    def is_prime_helper(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if is_prime_helper(result):
            print("Простое")
        else:
            print("Составное")
        return result

    return wrapper


@is_prime
def sum_three(*numbers):
    k = 0
    for i in numbers:
        k += i
    return k


n = sum_three(2, 3, 2)
print(n)
