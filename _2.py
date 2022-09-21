#задание1

a = True
b = False
print(a and b)
print((a and b) or b)
print((a and b) or not (a and b))
print(a and b or not (a or b) or b)
print(b and b or not a and (a or b or a) or not (a or b))
print(1 << 2)
print(1 & 0 | 1 >> 1)
print(1 & 0 | 1 >> 0)
print(0b101 & 0b111 ^ 0b111 | 0b010)


#задание2

print('введите два числа для сравнения:')
a = int(input())
b = int(input())
if a > b:
    print('наименьшее число:' + ' ' + str(b))
elif a == b:
    print('эти числа равны между собой')
else:
    print('наименьшее число:' + ' ' + str(a))



#задание3

print('введите три числа для сравнения:')
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('эти числа равны между собой')
else:
    print('наибольшее число:' + ' ' + str(max(a, b, c)))


#задание4

print('введите три числа:')
a = int(input())
b = int(input())
c = int(input())
if a == b and a == c:
    print('уникальных чисел нет, все числа равны ' + str(a))
elif a != b and b == c:
    print('кол-во уникальных чисел: 1' + '  ' + 'это число - ' + str(a))
elif c != b and b == a:
    print('кол-во уникальных чисел: 1' + '  ' + 'это число - ' + str(c))
elif a == c and a != b:
    print('кол-во уникальных чисел: 1' + '  ' + 'это число - ' + str(b))
else:
    print('кол-во уникальных чисел: 3' + '  ' + 'это числа: ' + str(a) + ', ' + str(b) + ', ' + str(c))