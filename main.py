# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置
import math
import sys
from typing import List

'''

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


# message = input('tell me something:')
# print(message)
# a = 10
# b = 3
# a += b        # 相当于：a = a + b
# a *= a + 2    # 相当于：a = a * (a + 2)
# print(a)      # 算一下这里会输出什么
#
# oe=input('odd even')
# oe=int(oe)
# if oe % 2 == 0:
#     print('even')
# else:
#     print('odd')
# print(oe)

# current_number = 1 #while 循环
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
# message = ''
# while message != 'quit':
#     message = input("复读机，输入quit 退出")
#     if message != 'quit':
#         print(message)


current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue #只要奇数
    print(current_number)

sandwich_order = ['a','b','c','a','a']

finished_sandwiches = []
for x in sandwich_order:  #因为在循环中更改列表的大小，循环的范围也会改变。
    if x == 'a':
        sandwich_order.remove('a')
print(sandwich_order)

sandwich_order = ['a','b','c','a','a']
while 'a' in sandwich_order:  #此处判断多次，所以避免了循环范围的改变
    sandwich_order.remove('a')
print(sandwich_order)

if 'a' in sandwich_order:
    print("还有a")
else:
    print("a无了")

while sandwich_order:
    fresh_sandwich = sandwich_order.pop()
    print(fresh_sandwich+" sandwich is finished.")
    finished_sandwiches.append(fresh_sandwich)

print("here is your sandwiches")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title() + " sandwich")

# active = True
# while active:
#     message = input()
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

current_number =0
while current_number < 10:
    if current_number % 2 != 0:
         print(current_number)
    current_number += 1

def greet_user():
    """xiansh"""
    print("hello")
greet_user()
'''

# def greet_user(username):
#     print("hello,"+username.title()+"!")
#
# greet_user('jesse')
#
#
# a = ''
# if bool(a) == False:
#     print("false")
#
# def build_name(first,last,age=''):
#     person={'first': first,'last':last}
#     if age:
#         person['age'] = age
#     return person
#
# muscian = build_name('jimi','ffff')
# print(muscian)
#
# g = float(input("77.5555"))
# c = (g - 32) / 1.8
# print(f'{g:.2f} 华氏度')
# '''太重要了这里, 一定要有一个点在数据格式前面'''
# print('%.1f' %g)
# g = float(input('请输入华氏温度: '))
# c = (g - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (g, c))
# print(f'{g:.1f}华氏度 = {c:.1f}摄氏度')
#
# row = int(input('请输入行数: '))
#
# for i in range(row):    #最后一个值不赋予 ，所以相当于你输入数字多少就循环多少次，此处已经计算了0的时候
#     for j in range(row): #全都是从零开始，当然也可以想象从1开始，带上最后一个值，前提是要循环之间互相嵌套作为变量而不是作为数值
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()
#
# for i in range(row):
#     for _ in range(i+1):
#         print('*',end="")
#     print()
# c = 2568//100
# print('%dchangdu' %(c))
# print('%.1fcccc'%c)
'''
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print("公鸡：%d只，母鸡：%d只，小鸡%d只" % (x, y, z))

# 生成斐波那契数列
num = int(input("fibonacci sequence top X:"))

# 找出10000以内的完美数
x = 1
behind = 1
for _ in range(num):
    if _ < 2:
        print(1, end=",")
    else:

        for _ in range(num - 2):
            behi2 = behind
            behind = x
            x = behind + behi2
            print(x, end=",")
        break
print()
'''
'''
def SuJduge(num):
    is_prime = True
    for i in range(2,int(math.sqrt(num))+1):   # for i in range(1,num//2):
        if num %i  == 0:
            is_prime = False
            break
    return is_prime





#
#
#
#
#
#
# def FacSum(m):
#     sum = 0
#     for i in range(1, m):
#         if m % i == 0:
#             sum += i
#     return sum
#
#
# yes = True
# while yes:
#     per = int(input("输入范围内的完美数:"))
#     if per > 0:
#         yes = False
#     else:
#         print('请输入正确范围')
#
# for _ in range(1, per+1):
#     if _ == FacSum(_):
#         print(_, end=',')
#
# print()

# yes = True
# while yes:
#     su = int(input("输入范围内的素数:"))
#     if su > 0:
#         yes = False
#     else:
#         print('请输入正确范围')
#

su = int(input("输入范围内的素数:"))

for i in range(2,su+1):
    if SuJduge(i):
        print(i,end=',')
print()

# 尝试计算
# 根据前面提到的各个概率以及这一赌博的规则
# 可以计算出掷骰方获胜的机会为 244/495，即 49．3％左右。
# from random import randint
#
# money = 1000
# top   = 1000
# while money > 0:
#     print('你的总资产为:', money)
#     if money > top:
#         top = money
#     needs_go_on = False
#     while True:
#         debt = int(input('请下注: '))
#         if 0 < debt <= money:
#             break
#     first = randint(1, 6) + randint(1, 6)
#     print('玩家摇出了%d点' % first)
#     if first == 7 or first == 11:
#         print('玩家胜!')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('庄家胜!')
#         money -= debt
#     else:
#         needs_go_on = True
#     while needs_go_on:
#         needs_go_on = False
#         current = randint(1, 6) + randint(1, 6)
#         print('玩家摇出了%d点' % current)
#         if current == 7:
#             print('庄家胜')
#             money -= debt
#         elif current == first:
#             print('玩家胜')
#             money += debt
#         else:
#             needs_go_on = True
# print('你破产了, 游戏结束!')
# print('最高筹码%d'%top)

m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fm_n = 1
for num in range(1, m - n + 1):
    fm_n *= num
print(fm // fn // fm_n)

#优化
import math
m = int(input('m = '))
n = int(input('n = '))
print(math.factorial(m)/math.factorial(n)/math.factorial((m-n)))

def gcd(x,y):
    (x,y) = (y,x) if x > y else (x,y)
    for factor in range(x,0,-1):
        if x % factor == 0 and y % factor == 0:
            return factor
def lcm(x,y):
    return x * y /gcd(x,y)

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
       total = temp % 10 + total * 10
       temp //= 10
    return total == num
'''
#
# s1 = '\'hello, world!\''
# s2 = '\n\\hello, world!\\\n'
#
# print(s1, s2, end='')
# s1 = '\141\142\143\x61\x62\x63'
# s2 = '\u9a86\u660a'
# print(s1, s2)
# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')
#
# str1 = 'hello, world!'
# # 通过内置函数len计算字符串的长度
# print(len(str1)) # 13
#
# print(str1.find('d'))
# # 将字符串以指定的宽度居中并在两侧填充指定的字符
# print(str1.center(50, '*'))
# # 将字符串以指定的宽度靠右放置左侧填充指定的字符
# print(str1.rjust(50, ' '))
#
# str2 ='   jackfrued@163.com '
# print(str2)
# print(str2.strip())
# str3 = 'abc123456'
#
# print(str3.isdigit())
# print(str3.isalpha())
# print(str3.isalnum())
# a, b = 5, 10
# print('%d * %d = %d' % (a, b, a * b))
# #简化
#
# a, b = 5, 10
# print(f'{a} * {b} = {a*b}')
#
# list1 = [1, 3, 5, 7, 100]
# for index in range(len(list1)):
#     print(list1[index])
#
# for index, elem in enumerate(list1):
#     print(index, elem)
# print(list1)
#
# list1 = [1, 3, 5, 7, 100]
# # 添加元素
# list1.append(200)
# print(list1)
# list1.insert(1, 400)
# # print(list1)
# # list1.extend([1,11,111,1111])
# print(list1)
# list1 += [1,11,111,1111]
# print(list1)
#
# if 1234 in list1:
#     list1.remove(1234)
# print(list1)
# if 3 in list1:
# 	list1.remove(3)
# print(list1)
# print(sys.getsizeof(list1))
# f = [x ** 2 for x in range(1, 1000)]
# print(sys.getsizeof(f))
#
#
# #为什么使用yield
# # 生成器实现
# def foo(num):
#     print("starting...")
#     while num<10:
#         num=num+1
#         yield num
#
# for n in foo(0):
#     print(n)
# #############range 和 yield 对比
# for n in range(10):
#     a=n
#     print(a) # 相当于 return a
# print("*" * 100)
#
# for n in range(10):
#      a = n
#      print(a)
#
# def foo1(num):
#     while num < 100:
#         num = num +1
#         yield num
#
# for n in foo1(0):
#     print(n)
#
# # 创建集合的字面量语法
# set1 = {1, 2, 3, 3, 3, 2}
# print(set1)
# print('Length =', len(set1))
# # 创建集合的构造器语法(面向对象部分会进行详细讲解)
# set2 = set(range(1, 10))
# set3 = set((1, 2, 3, 3, 2, 1))
# print(set2, set3)
# # 创建集合的推导式语法(推导式也可以用于推导集合)
# set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
# print(set4)
#
# set1.add(4)
# set1.add(5)
# set2.update([11, 12])
# set2.discard(5)
# if 4 in set2:
#     set2.remove(4)
# print(set1, set2)
# print(set3.pop())
# print(set3)
#
# # 创建字典的字面量语法
# scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
# print(scores)
# # 创建字典的构造器语法
# items1 = dict(one=1, two=2, three=3, four=4)
# # 通过zip函数将两个序列压成字典
# items2 = dict(zip(['a', 'b', 'c'], '123'))
# # 创建字典的推导式语法
# items3 = {num: num ** 2 for num in range(1, 10)}
# print(items1, items2, items3)
# # 通过键可以获取字典中对应的值
# print(scores['骆昊'])
# print(scores['狄仁杰'])
# # 对字典中所有键值对进行遍历
# for key in scores:
#     print(f'{key}: {scores[key]}')
# # 更新字典中的元素
# scores['白元芳'] = 65
# scores['诸葛王朗'] = 71
# scores.update(冷面=67, 方启鹤=85)
# print(scores)
# if '武则天' in scores:
#     print(scores['武则天'])
# print(scores.get('武则天'))
# # get方法也是通过键获取对应的值但是可以设置默认值
# print(scores.get('武则天', 60))
# print(scores)
# # 删除字典中的元素
# print(scores.popitem())
# print(scores.popitem())
# print(scores.pop('骆昊', 100))
# print(scores)
# # 清空字典
# scores.clear()
# print(scores)
#
# from math import sqrt
#
#
# class Point(object):
#
#     def __init__(self, x=0, y=0):
#         """初始化方法
#
#         :param x: 横坐标
#         :param y: 纵坐标
#         """
#         self.x = x
#         self.y = y
#
#     def move_to(self, x, y):
#         """移动到指定位置
#
#         :param x: 新的横坐标
#         "param y: 新的纵坐标
#         """
#         self.x = x
#         self.y = y
#
#     def move_by(self, dx, dy):
#         """移动指定的增量
#
#         :param dx: 横坐标的增量
#         "param dy: 纵坐标的增量
#         """
#         self.x += dx
#         self.y += dy
#
#     def distance_to(self, other):
#         """计算与另一个点的距离
#
#         :param other: 另一个点
#         """
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return sqrt(dx ** 2 + dy ** 2)
#
#     def __str__(self):
#         return '(%s, %s)' % (str(self.x), str(self.y))
#
#
# def main():
#     p1 = Point(3, 5)
#     p2 = Point()
#     print(p1)
#     print(p2)
#     p2.move_by(-1, 2)
#     print(p2)
#     print(p1.distance_to(p2))
#     print(Point.distance_to(p1,p2))
#
# if __name__ == '__main__':
#     main()
#

class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()
    import tkinter
    import tkinter.messagebox


    def main():
        flag = True

        # 修改标签上的文字
        def change_label_text():
            nonlocal flag
            flag = not flag
            color, msg = ('red', 'Hello, world!') \
                if flag else ('blue', 'Goodbye, world!')
            label.config(text=msg, fg=color)

        # 确认退出
        def confirm_to_quit():
            if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
                top.quit()

        # 创建顶层窗口
        top = tkinter.Tk()
        # 设置窗口大小
        top.geometry('240x160')
        # 设置窗口标题
        top.title('小游戏')
        # 创建标签对象并添加到顶层窗口
        label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
        label.pack(expand=1)
        # 创建一个装按钮的容器
        panel = tkinter.Frame(top)
        # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
        button1 = tkinter.Button(panel, text='修改', command=change_label_text)
        button1.pack(side='left')
        button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
        button2.pack(side='right')
        panel.pack(side='bottom')
        # 开启主事件循环
        tkinter.mainloop()


    if __name__ == '__main__':
        main()


import Pygame


def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()