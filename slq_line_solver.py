mat = [[int(num) for num in input().split()] for _ in range(int(input()))]
my_sol = [(f:=lambda m, k: f([list(map(lambda x, y: y - x*m[row][k]/m[next((i for i, el in enumerate(m) if el[k] != 0 and not any(el[:k])), None)][k], m[next((i for i, el in enumerate(m) if el[k] != 0 and not any(el[:k])), None)], m[row])) if row != next((i for i, el in enumerate(m) if el[k] != 0 and not any(el[:k])), None) else list(map(lambda x: x/m[next((i for i, el in enumerate(m) if el[k] != 0 and not any(el[:k])), None)][k], m[next((i for i, el in enumerate(m) if el[k] != 0 and not any(el[:k])), None)]))  for row in range(0, len(m))], k+1) if k != len(mat) else m)(mat, 0)[i][-1] for i in range(len(mat))]
[print(x) for x in my_sol]

"""
    next((i for i, el in enumerate(m) if el[k] != 0 and not any(el[:k])         finds first row with nonzero pivot that has zeros before the pivot
    y - x*m[row][k]/m[index_determined_above][k], m[index_determined_above], m[row])), m[row])) if row != index_determined_above else list(map(lambda x: x/m[index_determined_above)][k], m[index_determined_above]))           subract corresponding multiple of the row from other rows, if same row divide by pivot so that pivot is one
    (f:=lambda m, k: f(function_that_does_row_subtraction, k)(for row in range(0, len(m))], k+1) if k != len(mat) else m)(mat, 0)           recursive formula for lambda, k means column to be eliminated, original input is given matrix "mat"
"""
