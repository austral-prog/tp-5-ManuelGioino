import math

def roots(a, b, c):
    determinante = b**2 - 4*a*c
    if determinante < 0:
        return "( )"
    elif determinante == 0:
        return f"({-b/2})"
    elif determinante > 0:
        root_1 = (-b + math.sqrt(determinante))/2
        root_2 = (-b - math.sqrt(determinante))/2
        return f"({root_1}, {root_2})"

 
def value_y(a, b, c, x):
    return a*x**2 + b*x + c



def to_string(a, b, c):
    if a == 0 and b != 0 and c!= 0:
        return f"f(x) = {b} * X + {c}"
    elif a != 0 and b == 0 and c != 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif a != 0 and b != 0 and c == 0:
        return f"f(x) = {a} * X^2 + {b} * X"
    elif a == 0 and b == 0 and c != 0:
        return f"f(x) = {c}"
    elif a == 0 and b != 0 and c == 0:
        return f"f(x) = {b} * X"
    elif a != 0 and b == 0 and c == 0:
        return f"f(x) = {a} * X^2"
    elif a == 0 and b == 0 and c == 0:
        return f"f(x) = 0"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"

def derivation(a, b, c):
    if a and b:
        return f"f'(x) = {2 * a} * X + {b}"
    elif not a:
        return f"f'(x) = {b}"
    elif not b:
        return f"f'(x) = {2 * a} * X"
