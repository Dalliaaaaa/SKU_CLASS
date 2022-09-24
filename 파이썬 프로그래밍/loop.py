#3이 들어간 횟수 세기

total = 0

# for i in range(1, 10000, 1):
for i in range(1, 10**6+1):
  var = str(i).count('3')
  total = total + var

print(total)

