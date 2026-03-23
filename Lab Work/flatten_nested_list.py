nested = [[1, 2], [3, 4], [5]]

result = [i for sub in nested for i in sub]
print(result)
