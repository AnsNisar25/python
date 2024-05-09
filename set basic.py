Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> set3={}
>>> print(set3)
{}
>>> print(type(set3))
<class 'dict'>
>>> set3=set(range(1,10))
>>> print(set3)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> set3.add(56)
>>> print(set3)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 56}
>>> set.pop()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set.pop()
TypeError: unbound method set.pop() needs an argument
>>> set3.pop()
1
>>> print(set3)
{2, 3, 4, 5, 6, 7, 8, 9, 56}
set3.pop(8)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    set3.pop(8)
TypeError: set.pop() takes no arguments (1 given)
set.remove(8)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    set.remove(8)
TypeError: descriptor 'remove' for 'set' objects doesn't apply to a 'int' object
set3.remove(56)
print(set3)
{2, 3, 4, 5, 6, 7, 8, 9}
set3.clear()
print(set3)
set()
set3={12,32,45,56,76,34,23,57,66,89,66}
set4={12,45,52,67,34,78,66,23,53,67,78}
print(set3.union(set4))
{66, 67, 12, 76, 78, 23, 89, 32, 34, 45, 52, 53, 56, 57}
print(set3.intersection(set4))
{34, 66, 12, 45, 23}
