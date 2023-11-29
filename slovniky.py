# utf
from collections import defaultdict
import random


def same_elems(a: list, b: list, repetition = False) -> bool:
    """
    Returns true if lists contains same elements
    
    If repetition = True, the lists must have same number of elements
    """
    def count_els(a: list):
            els = defaultdict(int)
            for el in a:
                els[el] += 1
            return els
    
    if repetition:
        a_count = count_els(a)
        b_count = count_els(b)
        for key in a_count.keys():
             if a_count[key] != b_count[key]:
                  return False
        return True
    else: 
        return set(a) == set(b) 

def n_grams(n: int, text: str) -> list:
    """
    Returns all n_grams with given frequency
    """
    n_grams_occurancies = defaultdict(int)
    for i in range(len(text)-n):
        n_grams_occurancies[text[i:i+n]] += 1
    return sorted(dict(n_grams_occurancies).items(), key = lambda x:x[1], reverse = True)


def n_grams_generator(n: int, text: str) -> list:
    n_grams_next = defaultdict(lambda: defaultdict(int))
    for i in range(len(text)-n-1):
        n_grams_next[text[i:i+n]][text[i+n+1]] += 1
    return dict(n_grams_next)


def generate_text(start: str, length: int, keys: dict, n: int) -> str:
    text = start
    for i in range(length):
        text += 


     

def get_text(path: str) -> str:
    text = ""
    for row in open(path, encoding="utf8"):
         text = text + row + "\n"
    return text
         

if __name__ == "__main__":
    # print(same_elems([1, 2, 3, 4, 1, 2], [1, 1, 2, 2, 3, 4], True))
    # print(n_grams(3, get_text("Y:\python\poe.txt")))
    print(n_grams_generator(2, "ahoj, ahne, ahojahoj joha noha "))
