#O(log(n))
def prime_number(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    a = 2  # Nilai a yang tetap untuk uji primalitas

    # Uji Primalitas Fermat dengan a=2
    if pow(a, n - 1, n) != 1:
        return False

    return True

if __name__ == '__main__':
    print(prime_number(1000000007)) # True
    print(prime_number(1500450271)) # True
    print(prime_number(1000000000)) # False
    print(prime_number(10000000019)) # True
    print(prime_number(10000000033)) # True
