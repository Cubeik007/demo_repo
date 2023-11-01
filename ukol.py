from typing import Optional
from math import sqrt

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
        
    
def histogram(my_list = []):
    my_dict = {}
    my_list 


print(quadratic(1, 4, 4))
# print(common_elements(sorted([8, 7, 12, 1, 5, 12]), sorted([3, 12, 1, 4, 6, 9, 11])))


        
         
