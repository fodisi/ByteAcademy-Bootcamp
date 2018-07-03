# https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem?h_r=next-challenge&h_v=zen

#!usr/bin/env python3

import sys

S = input().strip()
try:
    print(int(S))
except Exception:
    print('Bad String')
