Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#print pattern using nested loops
rows=5
#outer loop
for i in range(1, rows+1) :
    #inner loop
    for k in range(1, i+1) :
        print(" * ", end=" ")
    print("")

 *  
 *   *  
 *   *   *  
 *   *   *   *  
 *   *   *   *   *  
# hald pyramid with numbers
rows=5
for i in range(1, rows+1) :
...     for k in range(1, i+1):
...         print(k, end=" ")
...     print("")
... 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
>>> #inverted pyramid pattern with numbers
>>> rows=5
>>> a=0
>>> #reverse for loop from 5 to 0
>>> for i in range(rows,0,-1):
...     a+=1
...     for k in range(1,i+1):
...         print(a, end=" ")
...     print("")
... 
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 
#reverse
rows=6
for i in range(0,rows+1):
    for k in range(rows-i,0,-1):
        print(k, end=" ")
    print()

6 5 4 3 2 1 
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 

#right angle triangle
rows=6
for i in range(1,rows):
    num=1
    for k in range(rows,0,-1):
        if k>i:
            print(" ", end=" ")
        else:
            print(num, end=" ")
            num +=1
    print("")

          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 

#right angle triangle using stars
  
rows=4
k=2*rows-2
for i in range(0,rows):
    for j in range(0,k):
        print(end=" ")
    k=k-2
    for j in range(,i+1):
        
SyntaxError: invalid syntax
rows=4
k=2*rows-2
for i in range(0,rows):
    for j in range(0,k):
        print(end=" ")
    k=k-2
    for j in range(0,i+1):
        print()

      
    

  






#multiplication table
        
rowa=10
for in range(1,rows+1):
    
SyntaxError: invalid syntax
rowa=10
rows=10

============================== RESTART: Shell =============================
initial_velocity=0
final_velocity=10
time=20
acc=(final_velocity-initial_velocity)/time
print(acc)
0.5

============================== RESTART: Shell =============================
richter_magnitute=float(input("enter the value: "))
enter the value: 10
if richter_magnitute >1.0 and richter_magnitute <2.0:
    print("micro")
elif richter_magnitute>2.0 and richter_magnitute<4.0:
    print("very rarely damage")
elif richter_magnitute>4.0 and richter_magnitute<5.0:
    print("weak buildings")
elif richter_magnitute>5.0 and richter_magnitute<6.0:
    print("poorly constructed buildings")
elif richter_magnitute>6.0 and richter_magnitute<7.0:
    print("causes damage")
elif richter_magnitute>7.0 and richter_magnitute<8.0:
    print("damage to most buildings")
elif richter_magnitute>8.0 and richter_magnitute<9.0:
    print("destruction")
else:
    print("causes unbelievable damage")

causes unbelievable damage

i=100
while (i<=200)
SyntaxError: expected ':'
i=100
while (i<=200):
{}
SyntaxError: expected an indented block after 'while' statement on line 1
i=100
while (i<=200):
