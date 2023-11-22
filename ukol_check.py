
mat = [[int(num) for num in input().split()] for _ in range(int(input()))]
my_sol = [(f:=lambda m, k: f([list(map(lambda x, y: y - x*m[row][k]/m[next((i for i, el in enumerate(m) if el[k] != 0 and not any(el[:k])), None)][k], m[next((i for i, el in enumerate(m) if el[k] != 0 and not any(el[:k])), None)], m[row])) if row != next((i for i, el in enumerate(m) if el[k] != 0 and not any(el[:k])), None) else list(map(lambda x: x/m[next((i for i, el in enumerate(m) if el[k] != 0 and not any(el[:k])), None)][k], m[next((i for i, el in enumerate(m) if el[k] != 0 and not any(el[:k])), None)]))  for row in range(0, len(m))], k+1) if k != len(mat) else m)(mat, 0)[i][-1] for i in range(len(mat))]
[print(x) for x in my_sol]
