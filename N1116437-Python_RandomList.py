import random
#輸入
random.seed(int(input()))
mlist = random.sample(range(100), 20)
print(mlist)

print((mlist[0]+mlist[1]+mlist[2]+mlist[3]+mlist[4])-(mlist[-5]+mlist[-4]+mlist[-3]+mlist[-2]+mlist[-1]))
print(sum(mlist[:5])-sum(mlist[-5:]))