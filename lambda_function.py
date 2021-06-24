#lambda function :- Anonymous function

l1=[3,2,3,4,5,56,6]

print(list(map(lambda x: x%2==0,l1)))
print(list(filter(lambda x: x%2==0,l1)))