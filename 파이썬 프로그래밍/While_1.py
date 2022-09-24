# sum = 0
# count = 1
# n = int(input("원하는 숫자를 입력하세요: "))

# while count <= n:
#   sum += count
#   count += 1

# print("지정한 숫자까지의 합계 : ", sum)

print(sum([1,2,3]))
tmp3 = list(range(1, 10**6+1))
print(sum(tmp3))

ex = sum(list(range(1,100+1,4)))
print(ex)