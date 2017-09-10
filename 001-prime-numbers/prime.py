# Sieve of Eratosthenes: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def SieveofEratosthenes(limit):
    # Initialize the primality list
    primality = [True] * limit
    for i in range(2, limit):
        if primality[i]:
            # return the prime number immediately
            yield i
            # mark i-factors non-prime
            for j in range(i*i, limit, i):
                primality[j] = False
    # return [i for i, isPrime in enumerate(primality) if isPrime is True]


# Example
primeNumbers = SieveofEratosthenes(100)
for prime in primeNumbers: print(prime)