def dot_product(a, b):
    return sum([(i*j) for i, j in zip(a, b)])


print(dot_product([1,2,3,4], [-3,-1,0,2])) # result = 3
print(dot_product([-1,0,1], [1,0,-1])) # result = -2