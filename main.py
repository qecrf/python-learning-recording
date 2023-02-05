# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置
from typing import List

cars = ['a', 'c', 'z', 'e']
print(cars)
print(sorted(cars))
print(sorted(cars, reverse=True))
# sorted 临时修改顺序的方法
cars.reverse()
print(cars)
print(len(cars))
print(cars[-1])
print(cars[0])
for car in cars:
    print(car.title() + " is mine");
    print("I can't wait to see you,my " + car.title() + "\n");
# 注意换行为反斜杠
for number in range(1, 6):
    print(number);
number = list(range(2, 11, 2))
print(number);

squares = []
for xx in range(1, 11):
    square = xx ** 2
    squares.append(square)
print(squares)

squares = []
for xxx in range(1, 11):
    squares.append(xxx ** 2)
print(squares)

number = list(range(1, 6))
print(number);

digits = list(range(1, 10))
digits.append(0)
print(digits)
digits[0] = 1000
print(digits)
digits.insert(1, 1)
print(digits)
print(min(digits));

xxxx = []
for value in range(1, 11):
    xxxx.append(value ** 2)
print(xxxx);

# 简略版
nm = [sq ** 2 for sq in range(1, 11)]
print(nm);

print(list(range(1, 21)));

final = []
for number in range(1, 21):
    print(number)
    final.append(number)
print(final);

odd = []
for number in range(1, 21, 2):
    odd.append(number)
print(odd);

million = list(range(1, 1000001))
print(max(million));

three = []
for number in range(3, 31, 3):
    three.append(number)
print(three);
# 立方 (cube)
cube = [number ** 3 for number in range(1, 11)]
print(cube);



cubeanalyze = [m + n for m in 'abcd' for n in 'efgh']

print([m + n for m in 'abcd' for n in 'efgh']);

print([m + n for m in 'acvb' for n in 'efgg'])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
# '%'这个是取模
print([x for x in range(1, 11) if x % 2 == 0])

print(4 ** 4)
print(pow(4, 4))

# first
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
for x in L1:
    if isinstance(x, str):
        L2.append(x.lower())
print(L2)
# sencond
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)

# if else
L2 = []
for x in range(1, 11):
    if x % 2 == 0:
        L2.append(x)
    else:
        continue
print(L2)

# 只有if
L3 = [x for x in range(1, 11) if x % 2 == 0]
print(L2)

# 从0开始 没有取到4
print(L3[:4])
print(L1[1:])

print("here is my car")
for car in cars[:3]:
    print(car.title())

print("here is my car")
print([car.title() for car in cars[:3]])

# 区分
cars1: list[str] = []
cars1 = cars
print(cars)
print(cars1)
cars.append('xxx')
cars1.append('xxxx')
print(cars)
print(cars1)
#
cars1 = []
cars1 = cars[:]
print(cars)
print(cars1)
cars.append('xxx')
cars1.append('xxxx')
print(cars)
print(cars1)

for car_1 in cars1:
    print(car_1)

hundred = (1, 111, 11111, 111111)
print(hundred)

hundred = (3)
print(hundred)

hundred = (0, 11, 111)
print(hundred)
# 这里有提示 元组不可以赋值
# hundred[0] = 2 这里是错误的
print(hundred)

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("stop the anchovies")
if 'mushrooms' in requested_topping:
    print('True')

car = 'subaru'
print("Is car == 'audi'? I predict is True")

year = 65
if year < 18:
    print("未成年")
elif year < 65:
    print("成年")
else:
    print("老年")

alien_colors = 'green'
if alien_colors == 'green':
    print(5)
else:
    print(10)

#if 语句 将在列表至少有一个元素师访问TRUE,否则返回FALSE

requested_toppings=['miao']
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding "+ requested_topping+".")
    print("\n\n\tFinishing making your pizza!")
else:
    print("plain!")

alien_0 = {
    'color':'green',
    'point':5,
    }
print(alien_0)
del alien_0['point']
print(alien_0)

tinydict = {'mioa':'www.google.com','Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
for key,value in tinydict.items():
    print (key,value)

for value in set(tinydict.values()):
    print(value)

for value in tinydict.values():
    print(value )

for web in tinydict.keys():
    print(web.title())


#import this

import turtle

turtle.pensize(3)
turtle.pencolor('red')

for x in range(100):
    turtle.forward(100-x)
    turtle.right(30)


turtle.mainloop()

a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'complex'>
print(type(d))    # <class 'str'>
print(type(e))    # <class 'bool'>

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))


