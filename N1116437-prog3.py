#列出質數
num = int(input('請輸入整數:'))
for n in range(2,num):
  isPrime = True
  for i in range(2,n):
        if n %  i==0:
         isPrime = False
         break
  if isPrime:
     list1 = int(j) for j in range n


