def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def div(n1, n2):
    return n1 / n2


def cal(n1, n2, func):
    return func(n1, n2)


result = cal(2, 3, sub)
print(result)

