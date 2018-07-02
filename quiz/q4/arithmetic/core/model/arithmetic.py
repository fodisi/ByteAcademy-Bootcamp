#!/usr/bin/env python3


class Arithmetic():
    def __init__(self, operation, num1, num2):
        if operation.lower() not in ['add', 'subtract', 'multiply', 'divide']:
            raise Exception('Not supported operation.')
        self.operation = operation.lower()
        self.num1 = float(num1)
        self.num2 = float(num2)

    def sum(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    def to_str(self):
        parser = {'add': '+',
                  'subtract': '-',
                  'multiply': '*',
                  'divide': '/'}
        return '{0} {1} {2}'.format(self.num1, parser[self.operation], self.num2)

    def calculate(self):
        if self.operation == 'add':
            return self.sum()
        elif self.operation == 'subtract':
            return self.subtract()
        elif self.operation == 'multiply':
            return self.multiply()
        elif self.operation == 'divide':
            return self.divide()
        else:
            raise Exception('Not supported operation.')

    def to_dictionary(self):
        return {'expression': self.to_str(), 'result': str(self.calculate())}
