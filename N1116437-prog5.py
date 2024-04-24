# i = int(input('請輸入整數:'))
#j = int(input('請輸入整數:'))

#for i in range(1,i):
#for j in range(1,j):
#        print("*",end='')
#    print() 

num1 = int(input())
num2 = int(input())

if num1 < num2:
    for i in range(num1,num2+1):
        print(' ' * (num2-i),end='')
        print('*' * i)
elif num1 > num2:
    for i in range(num1,num2-1,-1):
        print(' '*(num1-i),end='')
        print('*' * i)
else:
    print('*' * num1)