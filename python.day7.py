Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list1=[10,45,54,23,67,23,76,87,23,54,76,34,65]
print(list1)
[10, 45, 54, 23, 67, 23, 76, 87, 23, 54, 76, 34, 65]
list1[2:10:2]
[54, 67, 76, 23]
#slice[startindex:stopindex:increment]
list1[-2:-4]
[]
list[-2:4]
list[slice(-2, 4, None)]
list1[2:-5]
[54, 23, 67, 23, 76, 87]
#mutuble ---can add or remove anytime
list1=[10,45,54,23,67,23,76,87,23,54,76,34,65,54,234,65,2545,234]
print(list1)
[10, 45, 54, 23, 67, 23, 76, 87, 23, 54, 76, 34, 65, 54, 234, 65, 2545, 234]
list2=['ajkdh','dhas','kad','kgds','adghjk']
for my in list2 :
    print(my)

    
ajkdh
dhas
kad
kgds
adghjk
for my in list2 :
    print(my.upper())

    
AJKDH
DHAS
KAD
KGDS
ADGHJK
print(list2.count('dhas'))
1
price=[125.4,56.78]
total=1
for pp in price :
    total*=pp
    print("total value of {} is {}".format(price,total))

total value of [125.4, 56.78] is 125.4
total value of [125.4, 56.78] is 7120.212
num=12
L1=[1,2,3,4,5,6]
L2=[7,8,9,2,7,1]
id(11)
140728352127736
id(L1)
2648214262784
id(L2)
2648214270336
L3=L1+L2
print(L3)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 7, 1]
#repetition operator
>>> print(L2*2)
[7, 8, 9, 2, 7, 1, 7, 8, 9, 2, 7, 1]
>>> #comparision operator
>>> print(L1<L2)
True
>>> print(L2<L3)
False
>>> L4=['f','d','d','g','t','w']
>>> L5=['d','f','s','d','d','d']
>>> print(L4>L5)
True
>>> #comparision based on ascii values
>>> print(L3.count('d'))
0
>>> print(L3.len())
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(L3.len())
AttributeError: 'list' object has no attribute 'len'
>>> print(len(L2))
6
