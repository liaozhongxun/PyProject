# 九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print(j, '*', i, "=", i * j, sep='', end='  ')
        else:
            print();
            break

print(10);
print("=======================================================")
# *三角形
sjxi = 1
while sjxi <= 5:
    print("*" * sjxi)
    sjxi += 1

one = 0
while one <= 5:
    one += 1
    two = 0
    while two <= 5:  # 直接two<one 不需要if了
        two += 1
        if one >= two:
            print("*", end=" ")
    print()
