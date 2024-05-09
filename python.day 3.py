Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
info = "
SyntaxError: unterminated string literal (detected at line 1)
info = "Learn python")
SyntaxError: unmatched ')'
info = ("Learn python")
if info=="Learn":
    print("good morning")
elif info=="program":
    print("good afternoon")
elif info=="LearnProgram":
    print("iam learning python")
else:
    print("invalid")

    
invalid
info = ("Learn python")
if info=="Learn":
    print("good morning")
elif info=="program":
    print("good afternoon")
elif info=="Learn Program":
    print("iam learning python")
else:
    print("invalid")

    
invalid

============================== RESTART: Shell =============================
info = ("Learn python")
if info=="Learn":
    print("good morning")
elif info=="program":
    print("good afternoon")
elif info=="Learn python":
    print("iam learning python")
else:
    print("invalid")

    
iam learning python
#calculating leap year
year=int(input("enter year"))
enter year2021
if (year%4==0) :
    if(year%400==0):
        print("its a leap year")
    else:
        print("its not leap year")
   else:
       
SyntaxError: unindent does not match any outer indentation level
#calculating leap year
year=int(input("enter year"))
enter year2021
if (year%4==0) :
    if(year%100==0):
        if(year%400==0):
            print("its a leap year")
        else:
            print("its not leap year")
    else:
        print("its an leap year")
else:
    print("its not leap year")

    
its not leap year

============================== RESTART: Shell =============================
price = int(input("enter price "))
enter price 500
quantity = int(input("enter quantity "))
enter quantity 10
amount = price*quantity
print(amount)
5000
if amount>200:
    print("hi")
else:
    print("hiii")
if amount>1000:
    
SyntaxError: invalid syntax
if amount>200:
    if amount>1000:
        print("hi")
    else:
        if amount<1000 and amount>600:
            print("good")
        elif amount<600 and amount>400:
            print("hello")
        else:
            print("very good")

        
hi
price = int(input("enter price "))
enter price 500
price = int(input("enter price"))
enter price
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    price = int(input("enter price"))
ValueError: invalid literal for int() with base 10: ''
>>> price = int(input("enter price "))
enter price 500
>>> quantity = int(input("enter quantity "))
enter quantity 1
>>> if amount>200:
...     if amount>1000:
...         print("hii")
...     else:
...         if amount<=1000 and amount>600:
...             print("hello")
...         elif amount<=600 and amount>400:
...             print("hiii")
...         else :
...             print("my")
... elif amount==200:
...     print("haddd")
... else:
...     print("hhu")
... 
...     
hii
