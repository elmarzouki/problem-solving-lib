# Sieve of Eratosthenes: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def SieveofEratosthenes(limit):
    # Initialize the primality list
    primality = [True] * limit
    # excluding 0, 1 they ain't prime
    primality[0] = primality[1] = False
    for i, isPrime in enumerate(primality):
        if isPrime:
            # return the prime number immediately
            yield i
            # mark i-factors non-prime
            for j in range(i*i, limit, i):
                primality[j] = False
    # return [i for i, isPrime in enumerate(primality) if isPrime is True]


# Example
primeNumbers = SieveofEratosthenes(100)
for prime in primeNumbers: print(prime)