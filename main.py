print("problem 1: ")

num = int(input("num: "))
num2 = num
count = int(input("count: "))
i = 1

while i <= count:
    print(num)
    num += num2
    i = i + 1

print("problem 2: ")

a = input("enter a string(in bulgarian): ")
b = 0

for i in a:
    if i == "а" or i == "ъ" or i == "о" or i == "у" or i == "е" or i == "и":
        b = b + 1

print(b)

print("problem 3: ")

list = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    elements = input("enter elements: ")

    list.append(elements)

j = 0

for j in list:
    if j.isdigit():
        list.remove(j)

print(list)

print("problem 4: ")

number = input("Enter a number: ")

if number == number[::-1]:
    print("true")
else:
    print("false")








