# # 90점 이상은 A
# # 70점 이상은 B
# # 40점 이상은 C
# # 39점 이하는 D

# score = int(input())

# if score >= 90:
#     print("A")
# elif score >= 70:
#     print("B")
# elif score >= 40:
#     print("C")
# else:
#     print("D")

# fruits = ['apple', 'pear', 'banana']

# for fruit in fruits:
#     print(fruit)

# for i in range(10):
#     print('Hello World', i)

# fruits = ['apple', 'pear', 'banana']

# for i, fruit in enumerate(fruits):
#     print(i, fruit)

t = int(input())

for i in range(t):
    a, b = map(int, input().split(' '))
    price_2017 = 0
    price_2018 = 0

    if a <= 0:
        price_2017 = 0
    elif a <= 1:
        price_2017 = 500
    elif a <= 3:
        price_2017 = 300
    elif a <= 6:
        price_2017 = 200
    elif a <= 10:
        price_2017 = 50
    elif a <= 15:
        price_2017 = 30
    elif a <= 21:
        price_2017 = 10
    else:
        price_2017 = 0

    if b <= 0:
        price_2018 = 0
    elif b <= 1:
        price_2018 = 512
    elif b <= 3:
        price_2018 = 256
    elif b <= 6:
        price_2018 = 128
    elif b <= 10:
        price_2018 = 64
    elif b <= 15:
        price_2018 = 32
    elif b <= 21:
        price_2018 = 16
    else:
        price_2018 = 0

    print((price_2017 + price_2018)*10000)