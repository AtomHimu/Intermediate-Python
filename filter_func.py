# filter function
li=[1,2,3,4,5,6]

def even(x):
    return x%2==0
print(list(filter(even,li)))

#map function
def square(x):
    return x**x
print(list(map(square,li)))