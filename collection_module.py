import collections
from collections import *

#Counter method :- create a dictionary
c=Counter('gallad')
print(c)
c=Counter(['a','b','c','a','c'])
print(c)
print(list(c.elements()))
print(c.most_common())
c=Counter(cats=4,dogs=5)
print(c)
print(list(c.elements()))
print(c.most_common())
c=Counter(a=4,b=5,c=0,d=6)
print(c)
d=['a','b','d','b','b']
# subtract method
c.subtract(d)
print(c)
# add method
c.update(d)
print(c)
#clear method
c.clear()
print(c)

# union and intersection method

##### namedtuple method in collections

point=namedtuple('Point',['x','y','z']) # take two parameters as an input 1. name(point) 2. variable for values(x,y,z)
#taking list as a one parameter
# now variable point act as class so we have make its object
#1.object 1
newp1=point([1,2,3],[4,5,6],[7,8,9])
print(newp1)

#2.object 2
newp2=point(1,2,3)
print(newp2)

# you can also print the individual values
print(newp1.x)
print(newp2.z)
print(newp1[1])

# you can also make dictionary
print(newp1._asdict())
# you can also all fiels of objects like (x,y,z)
print(newp1._fields)
# you can also use replace method with object
newp3=newp1._replace(x=[12,13,14])
print(newp3)

p2=point._make(['a','b','c']) # by this method you can change the value of the point which is acting like a class
print(p2)

#deque
d=deque('hello')
print(d)

# add element.
d.append('42')
print(d)

d.appendleft('yoiu')
print(d)

#pop item
d.pop()
print(d)

d.popleft()
print(d)

#clear the deque
d.clear()
print(d)

#extend
d.extend('456')
d.extend('hello')
print(d)

d.extend([1,2,3])
print(d)

d.extendleft('re')
print(d)