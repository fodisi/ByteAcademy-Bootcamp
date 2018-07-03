# https://www.hackerrank.com/challenges/30-interfaces/problem?h_r=next-challenge&h_v=zen


#!/usr/bin/env python3

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum_divisors = 0
        for div in range(1, n + 1):
            if n % div == 0:
                sum_divisors += div

        return sum_divisors


if __name__ == '__main__':
    n = int(input())
    my_calculator = Calculator()
    s = my_calculator.divisorSum(n)
    print("I implemented: " + type(my_calculator).__bases__[0].__name__)
    print(s)
