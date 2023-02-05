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
'''
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
