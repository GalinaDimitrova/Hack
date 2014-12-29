from random import randint, random, choice

operators = {
    '^': lambda a, b: pow(a, b),
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b}


def take_random_number():
    return randint(0, 10)


def random_operator():
    opeartor = choice(['+', '-', '/', '^', '*'])
    return opeartor


def expr_result(op, left, right):
    if op == '/' and right == 0:
        return 0
    result = round(operators[op](left, right), 1)
    return result


def make_expression():
    op = random_operator()
    left = take_random_number()
    right = take_random_number()
    expression = str(left) + " " + op + " " + str(right)
    result = expr_result(op, left, right)
    return expression, result
