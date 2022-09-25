arr1 = [1, 2, 3]
arr2 = [10, 5, 7]
arr3 = [arr2, arr1]
arr3 = sorted(arr3, key=lambda x: x[0])
print(arr3)