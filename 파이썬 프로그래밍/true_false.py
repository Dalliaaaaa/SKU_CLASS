print([False]*100)

tmp = [True]*10
print(tmp)

for i in range(2):
  tmp.insert(5, False)
print(tmp)

tmp1 = [True]*49+[False]*2+[True]*49
print("tmp1 : ", tmp1)
print(len(tmp1))

tmp = ['@']*30
print(tmp)