# coding:utf-8

# Lecture 1

# print("Hello World")
# print(2019)
# print(13.4)

# name = "James Bond" # A string
# age = 35 # An integer assignment
# height = 1.82 # A floating point assignment
# print(name)
# print(age)
# print(height)

# a = b = c = 5
# a, b, c = 10, -70, "cat"
# A = "60"  # 区分大小写
# 栗子 = 1
# print(a)
# print(b)
# print(c)
# print(A)
# print(栗子)  # 字符编码因为Python3解释器的默认编码已经从Python2的ASCII编码改为UTF-8编码，UTF-8编码支持任何Unicode字符串的写入
# # var56 valid; 56var not valid

# import keyword
# print(keyword.kwlist)
# # or use an the interpreter;
# help('keywords')

# π = 54675675
# print(π)
#
# ♥ = "Family"  # invalid character '♥'
# print(♥)

# 动态类型(dynamically typed)中函数的参数传递：f(x)是一个不可变(immutable)的对象，而g(x)是一个可变(mutable)的对象。
# https://www.cnblogs.com/vamei/archive/2012/07/10/2582795.html
# def f(x):
#     x = 100
#     print(x)
# def g(x):
#     x[0] = 100
#     print(x)
# a = 1
# b = [1, 2, 3]
# f(a)
# g(b)
# print(a, b)

# a = 100 # integer
# b = 100.0 # float point number
# c = "Hello" # string
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))

# cities = ["tokyo", "oslo", "dakar"]
# for c in cities:
#     if c == "dakar":
#         print("Found African City.")
#     print(".")

# # innacuracy of floating point arithmetic
# a = 1.2
# b = 1.0
# if ((a-b) == 0.2):
#     print("do something.")
# print("done.")
# # One possible solution
# a = 1.2
# b = 1.0
# e = 0.0000001 # epsilon
# if (0.2 - e <= (a-b) <= 0.2 + e):
#     print("do something.")
# print("done.")
# # Floating Point Arithmetic: Issues and Limitations
# # https://docs.python.org/2/tutorial/ oatingpoint.html

# print('This a “another” string')
# print("and 'another' string")
#
# # \n includes a line at the end
# print("This is a first line.\nThis is a second line.")
#
# print('Escaping the \' character')  # Output：Escaping the ' character
# print('Escaping the \" character')  # Output：Escaping the " character
# print('Escaping the \\n character')  # Output：Escaping the \n character

# print('''This string has a single (') and a double (") quote.''')
#
# print("""This is the first line
# This is the second line
# This is the third line""")

# # demo of string operators
# strA = "Hello "
# strB = "World!"
# print(strA + strB)  # strA和strB连在一起
# print(strA * 3)  # 重复3次
# print(strA[2])  # begins at index 0： l
# # string[i:j] 是从[i]到[j]前面，长度为j-i （其中不包含[j]）
# print(strA[1:3])  # character at index j = 3 is not included: el
# print('el' in strA)  # 输出Boolens：Ture
# print('hola' not in strA)  # 输出Boolens：Ture
# print(r"\n")  # 在使用字符串而不想去除掉一些特殊意义的字符进行转义，在字符串前加r
# print(r"D:\worksapce_python\20160426_cp\training")

# days = 7
# name = "Anna"
# age = 33
# height = 1.757456456
# num = 23423
# print("A week has %d days " % days)  # %d Integers
# print("Your name is %s, your age is %d, and your height is %.2f"
#       % (name, age, height))  # %s String; %f Floating point numbers; %.\< number of digits >f 固定位数的浮点数
# print("The value of %d in hexadecimal is %x" % (num, num))  # %x —— hex 十六进制 x/X的大小写代表了Hex的字母大小写

# id function
# a = "Hello"
# b = 45.5
# c = True
# d = 34.5 + 6j
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(78.98 + 62))  # type() can be applied to expressions as well
#
# print(id(a))
# print(id(b))
# print(id(c))

 # Converting integers to floats
a = 10
print(float(a))
# Converting floats to integers
b = 8.89
print(int(b))
# Converting numbers to strings
c = 787.44
print("The new string is " + str(c))
# Converting strings to numbers
d = "567.65"
print(float(d))


