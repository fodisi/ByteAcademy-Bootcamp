# https://www.hackerrank.com/challenges/30-more-exceptions/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


#!/usr/bin/env python3


class Calculator():
    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception('n and p should be non-negative')

        return n**p


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
