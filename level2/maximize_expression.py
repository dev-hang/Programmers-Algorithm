from itertools import permutations
import re

def maximize_expression(expression):
    answer = 0
    operation = []
    operations = list()

    if '*' in expression:
        operation.append('*')
    if '+' in expression:
        operation.append('+')
    if '-' in expression:
        operation.append('-')

    operations = list(permutations(operation))
    expression = re.split('([^0-9])', expression)

    copy = []
    cal = 0

    for operation in operations:
        copy = expression[:]
        for op in operation:
            while op in copy:
                idx = copy.index(op)
                a, b = int(copy[idx - 1]), int(copy[idx + 1])

                if op == '+':
                    cal = a + b
                elif op == '-':
                    cal = a - b
                elif op == '*':
                    cal = a * b

                copy[idx - 1] = cal
                copy = copy[:idx] + copy[idx + 2:]

        answer = max(answer, abs(int(copy[0])))

    return answer




print(maximize_expression("100-200*300-500+20")) # result = 60420
print(maximize_expression("50*6-3*2")) # result = 300