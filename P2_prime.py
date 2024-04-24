N  = int(input())

isfound = False
for n in range(N, 1, -1):
    for i in range(2,n):
        if n % i ==0:
            break
    else:
        isfound = True
    if isfound:
        print(n)
        break