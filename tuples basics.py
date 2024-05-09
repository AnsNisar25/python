Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tuplee=(1,2,3,4,13,54,6,3,63,65,3,24,65)
>>> print(tuplee)
(1, 2, 3, 4, 13, 54, 6, 3, 63, 65, 3, 24, 65)
>>> print(len(tuplee))
13
>>> print(tuplee[3])
4
>>> print(tuplee[-4])
65
>>> print(tuplee[2:6:1])
(3, 4, 13, 54)
>>> print(tuplee.count(3))
3
>>> print(tuplee.index(54))
5
>>> del tuplee
>>> print(tuplee)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(tuplee)
NameError: name 'tuplee' is not defined. Did you mean: 'tuple'?
tuplee=(1,2,3,4,13,54,6,3,63,65,3,24,65)
print(tuplee)
(1, 2, 3, 4, 13, 54, 6, 3, 63, 65, 3, 24, 65)
