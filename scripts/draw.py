# i = 1
# j = 1
# n = input('输入一个数：')
# while i <= int(n):
#     while j <= i:
#         print((int(n) - i)*' ' + (2*j-1) * '*')
#         j += 1
#     i += 1
# n = input('输入一个数字:')
# for i in range(1,6):
#     for j in range(0,1):
#         print((5-i)*' '+(2*i-1)*'*')
i = 1
j = 1
n = input('输入一个偶数：')
while i <= int(n):
    if int(n)//2 == 0 and i <= int(n)/2:
        while j <= i:
            print((int(n) - i)*' ' + (2*j-1) * '*')
            j += 1
    i += 1
