Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list3-
SyntaxError: invalid syntax
list3=[10,20,30,40,50,30,30,90,80,60,40]
print(list3)
[10, 20, 30, 40, 50, 30, 30, 90, 80, 60, 40]
list3=[10,20,30,40,50,30,30,90,80,60,40,50,40,40]
print(list3.count(5))
0
print(list3.count(40))
4
print(index(5))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(index(5))
NameError: name 'index' is not defined
print(list3(5))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(list3(5))
TypeError: 'list' object is not callable
print(list3[5])
30
#append -- adding new element to list
list3.insert(5,587)
print(list3)
[10, 20, 30, 40, 50, 587, 30, 30, 90, 80, 60, 40, 50, 40, 40]
#insert -- adding new element at specific index
list.insert(5,489)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list.insert(5,489)
TypeError: descriptor 'insert' for 'list' objects doesn't apply to a 'int' object
list3.insert(8,974)
print(list3)
[10, 20, 30, 40, 50, 587, 30, 30, 974, 90, 80, 60, 40, 50, 40, 40]
#append -- adding new element to list
list3.append(1000)
print(list3)
[10, 20, 30, 40, 50, 587, 30, 30, 974, 90, 80, 60, 40, 50, 40, 40, 1000]
#pop -- remove element from end of list
list3.pop()
1000
#pop --remove element from the specific index of list
list3.pop(5)
587
print(list3)
[10, 20, 30, 40, 50, 30, 30, 974, 90, 80, 60, 40, 50, 40, 40]
list3.pop(7)
974
print(list3)
[10, 20, 30, 40, 50, 30, 30, 90, 80, 60, 40, 50, 40, 40]
del list3
print(list3)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(list3)
NameError: name 'list3' is not defined. Did you mean: 'list'?
>>> list3=[10,20,30,40,50,30,30,90,80,60,40,50,40,40]
>>> print(list3)
[10, 20, 30, 40, 50, 30, 30, 90, 80, 60, 40, 50, 40, 40]
>>> print(sum(list3))
610
>>> print(min(list3))
10
>>> print(max(list3))
90
>>> #print(list[indexouter][indexnestedlist])
>>> list4=[1,2,3,4,5,[11,22,33,44],6,7,8,9]
>>> print(list4)
[1, 2, 3, 4, 5, [11, 22, 33, 44], 6, 7, 8, 9]
>>> print(list4[5])
[11, 22, 33, 44]
>>> print(list4[5][2])
33
>>> print(list4[9])
9
