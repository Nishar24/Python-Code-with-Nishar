>>> f = open('chai.py') <!-- yha pe hmne jo file bnaya h chai.py usko open kr k f name k variable me store kiya h -->
>>> f.readline()
'import time\n'
>>> 
>>> f.readline()
'print("Chai is here")\n'
>>> f.readline()
'\n'
>>> f.readline()
'username = "Nishar"\n'
>>> f.readline()
'print(username)\n'
>>> f.readline()
''
>>> f.readline()
''
>>> f.readline()
''
>>> 
<!-- __next__() Method -->
>>> f = open('chai.py')
>>> f.__next__()
'import time\n'
>>> 
>>> f.__next__()
'print("Chai is here")\n'
>>> f.__next__()
'\n'
>>> f.__next__()
'username = "Nishar"\n'
>>> f.__next__()
'print(username)\n'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    f.__next__()
    ~~~~~~~~~~^^
StopIteration
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    f.__next__()
    ~~~~~~~~~~^^
StopIteration
>>> 


<!-- Using for loop -->

>>> for line in open('chai.py'):
...     print(line)
... 
import time

print("Chai is here")

username = "Nishar"

print(username)

>>> 

>>> for line in open('chai.py'):
...     print(line, end='') <!-- beech me space nhi aayega end use krne pe -->
... 
import time
print("Chai is here")
username = "Nishar"
print(username)
>>> 

<!-- Using While loop -->

>>> f = open('chai.py')         
>>> while True:
...     line = f.readline()
...     if not line: break
...     print(line, end='')
... 
import time
print("Chai is here")
username = "Nishar"
print(username)
>>> 


<!-- iter() Method in List -->

>>> myList = [1, 2, 3, 4]
>>> I = iter(myList)
>>> I
<list_iterator object at 0x000001DFDE0E05B0>
>>> I.__next__()
1
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    I.__next__()
    ~~~~~~~~~~^^
StopIteration
>>> 

<!-- Checking -->
>>> f = open('chai.py')
>>> iter(f) <!-- is f  Same for only file not List -->
True
>>> iter(f) is f.__iter__()
True
>>> 

>>> myNewList = [1, 2, 3]
>>> iter(myNewList) is myNewList
False
>>> 

<!-- Dictionary -->

>>> D = {'a': 1, 'b': 2}
>>> for key in D.keys():
...     print(key)
... 
a
b
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x000001DFDEB384A0>
>>> next(I) <!-- This next is also equal to __next__() -->
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration
>>> 

<!-- Range -->

>>> range(5)
range(0, 5)
>>> R = range(5)
>>> R
range(0, 5)
>>> I = iter(R)
>>> next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next()
    ~~~~^^
TypeError: next expected at least 1 argument, got 0
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration
>>> 