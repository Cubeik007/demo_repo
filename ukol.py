from typing import Optional
from math import sqrt, cos, pi


def common_elements(f_list: list[int], 
                    s_list: list[int]) -> list[int]:
    """Takes two lists of ORDERED integers.
    Returns list of elements that are in both lists."""
    common = []
    pos1, pos2 = 0, 0
    while pos1 < len(f_list) and pos2 < len(s_list):
        a = f_list[pos1]
        b = s_list[pos2]
        if a == b:
            common.append(f_list[pos1])
            pos1 += 1
        elif a < b:
            pos1 += 1
        else:
            pos2 += 1
    return list(set(common))


def fibonaci(n: int) -> int:
    """returns n-th fibonatchi number"""
    if type(n) != int or n < 1:
        raise Exception("This is an invalid input, use positive number n please.")
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonaci(n-1)+fibonaci(n-2)


def quadratic(a: float, b = 0.0, c = 0.0) -> list[Optional[float]]:
    """returns solution of quadratic equations with coefficients a, b c"""
    if a == 0:
        raise Exception("This is not a quadratic equation")
    det = b**2-4*a*c
    if det < 0:
        return []
    else:
        dif = sqrt(det)
        return [(b+dif)/2*a, (b-dif)/2*a]
         

def histogram(my_str: str) -> dict:
    my_dict = {}
    my_set = set([i for i in my_str  if i.isalpha()])


def square_root(n: int) -> Optional[int]:
    """Returns a square root of number.

    If number is not integer or is negative, raises error.
    """
    if (type(n) is not int or n < 0):
        raise Exception("Your input is invalid, you can use integers only!")
    l = 0
    r = n

    while l <= r:
        mid = (l+r)//2
        guess = mid**2
        if guess == n:
            return mid
        elif guess < n:
            l = mid+1
        else: 
            r = mid-1
    return None


def x_cos_x() -> Optional[int]:
    """Returns a square root of number.

    If number is not integer or is negative, raises error.
    """
    
    l = 0
    r = 2*pi

    while l <= r:
        mid = (l+r)/2
        guess = round(mid-cos(mid), 4)
        if guess == 0:
            return mid
        elif guess < 0:
            l = mid
        else: 
            r = mid
    return None


def bubble_sort(x: list[int]) -> list[int]:
    """Returns ordered list using bubble sort."""

    my_len = len(x)-1
    i = 0
    for j in range(my_len):
        for i in range(my_len):
            if x[i]>x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    return x


def sorting_words(x: list[str], key=0) -> list[str]:
    """Returns lexicolographicaly sorted list."""

    my_len = len(x)-1
    i = 0
    for j in range(my_len):
        for i in range(my_len): 
            x[i], x[i+1] = x[i+1], x[i]
            if x[i][key]>x[i+1][key]:
                x[i], x[i+1] = x[i+1], x[i]
    check_list = []
    l = 0
    for i in range(my_len):
        if x[i][key] == x[i+1][key]:
            l += 1
        else:
            check_list.append(l)
    new_list = []
    key += 1
    for index in range(len(check_list)-1):
        new_list.append(sorting_words(x[check_list[index]:check_list[index+1]], key))
    return x


def reverse(s: str) -> str:
    """Returns reversed string."""
    return s[::-1]


def count_words(text: str, unique=True) -> int:
    "Returns number of words in given string"

    new_text = ""
    for i in text:
        if i.isalpha() or i == " ":
            new_text += i
    test_list = new_text.split()
    if unique:
        return len(set(test_list))
    else:
        return len(test_list)
    

def eval_string(text: str) -> float:
    "evaluate string"
    
    def eval_list(expression: list) -> float:
        bracket_counter = 0
        sub_expr = []
        new_expr = []
        expression.append("END")
        for el in expression:
            if el in ["+", "-", "END"]:
                my_num = sub_expr[0]
                for i, el2 in enumerate(sub_expr[1::2]):
                    if el2 == "*":
                        my_num = my_num*sub_expr[i+2]
                    if el2 == "/":
                        my_num = my_num/sub_expr[i+2]
                new_expr.extend([my_num, el])
                sub_expr = []
            else: 
                sub_expr.append(el)
        expression = new_expr
        my_num = expression[0]
        expression.pop()
        for i, el in enumerate(expression[1::2]):
            if el == "+":
                my_num += expression[2*i+1]
            if el == "-":
                my_num -= expression[2*i+1]
        return my_num

    operators = ["+", "-", "*", "/", "(", ")"]
    expression = []
    num = ""
    for i in text:
        if i in operators:
            expression.extend([float(num), i])
            num = ""
        else:
            num += i
    expression.append(float(num))
    print(eval_list(expression))
            
    
    

if __name__ == "__main__":
    print(eval_string("4+5/8+1.3"))

print(sorting_words(["jablko", "jahoda", "bagr", "bricho", "svedsko"]))
