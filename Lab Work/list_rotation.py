lst = [10, 20, 30, 40, 50]
k = 2

rotated = lst[-k:] + lst[:-k] #logic for rotating list
print(rotated)
