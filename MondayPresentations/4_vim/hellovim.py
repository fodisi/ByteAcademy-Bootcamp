#!/usr/env/bin python3

import os


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    msg = "Help! How do I exit Vim ???"
    print('{0}{1:^80}{0}'.format(5*'\n', msg))
    input()
