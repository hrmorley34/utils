from typing import Union


def is_prime_sqrt(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True


class PrimesArray:
    values: list
    max: int

    def __init__(self, initial=[2, 3, 5, 7, 11, 13, 17, 19]):
        " Create a PrimesArray with an initial list of primes "
        if initial:
            self.values = list(initial)
            self.max = int(initial[-1])
        else:
            self.values = [2]
            self.max = 2

    def __repr__(self) -> str:
        return "PrimesArray(length={}, max={})".format(len(self.values), self.max)

    def next(self) -> int:
        " Keep checking numbers until finding one "
        while True:
            p = self.max + 1
            for i in self.values:
                # Check each prime isn't a factor
                if p % i == 0:
                    break
                elif i >= p ** 0.5:
                    # If factor is more than the square root, there aren't any more
                    self.values.append(p)
                    self.max = p
                    return p
            self.max = p

    def calculate_up_to(self, number: int):
        " Cache all primes up to and including number "
        for p in range(self.max + 1, number + 1):
            for i in self.values:
                if p % i == 0:
                    break
                elif i >= p ** 0.5:
                    self.values.append(p)
                    break
            self.max = p

    def __contains__(self, number: int) -> bool:
        " x in PrimesArray -> is x prime? "
        if number > self.max:
            self.calculate_up_to(int(number))
        return number in self.values

    def is_prime(self, number: int) -> bool:
        " Check if number is prime "
        return number in self

    def __getitem__(self, key: Union[int, slice]) -> Union[list, int]:
        " PrimesArray[:10] -> the first 10 primes "
        if isinstance(key, slice):
            top = key.stop
        else:
            top = int(key) + 1
        while len(self.values) < top:
            self.next()
        return self.values.__getitem__(key)

    def __iter__(self):
        " Iterate infinitely through the prime numbers (from 2) "
        for p in self.values:
            yield p
        while True:
            yield self.next()


primes = PrimesArray()
is_prime = primes.is_prime
