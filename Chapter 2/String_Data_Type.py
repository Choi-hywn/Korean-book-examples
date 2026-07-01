food = "python's favorite food is perl" 
print(food) 
# If you want to use single or double quotes inside a string, use the other type of quote.

food = 'python\'s favorite food is perl'
print(food)
# (\'): during the string, you can use a backslash to escape the single quote.

multiline = "life is too short\nYou need python"
print(multiline)
# (\n): during the string, you can use a backslash to escape the new line.
# Escape = backslash(\): during the string, you can use a backslash to escape the backslash itself.

multiline = """
life is too short
You need python
"""
print(multiline)
# ("""): during the string, you can use triple quotes to create a multi-line string.

head = "Python"
tail = " is fun!"
print(head + tail)

a = "python"
print(a * 2)


print("=" * 50)
print("My Program")
print("=" * 50)

a = "Life is too short" 
print(len(a))
# (len): returns the length of the string.

a = "you need python"
print(len(a))

a = "Life is too short, You need python"
print(a[3])
# (a[3]): returns the character at index 3 of the string.
# indexing starts from 0, so a[3] returns the 4th character of the string.

a = "Life is too short, You need python"
print(a[0:4]) 
print(a[19:])
print(a[:17])
print(a[:])
# (a[0:4]): returns the substring from index 0 to 3 of the string. 
# The substring includes the character at index 0 but excludes the character at index 4.

num = 18
print("현재 온도는 %d도 입니다." % num)

apple = 3
print("I eat %d apples." % apple)
# (%d): is a format specifier that indicates that the value to be inserted is an integer.
# 문자열 포멧팅(format code): 문자열 안에 어떤 값을 삽입하는 방법 

print("I eat %s apples." % "three")
# (%s): is a format specifier that indicates that the value to be inserted is a string.
# 문자열 포멧팅 할때 문자열을 바로 삽입하고 싶을때는 "" 사용하여 넣는다

print("i ate %d apples. so i was sick for %s days." % (10, "three"))
# if you want to insert multiple values into a string, you can use a tuple to group the values together and pass them as a single argument to the format specifier.
# if you don't want to think about what kind of data type the value is, you can use %s to insert any type of value into the string.

print("Error is %d%%." % 98)
# if you want to include a percent sign in the string, you can use %% to escape the percent sign. 
# (%%): during the string, you can use double percent signs to escape the percent sign.
# 일반 문자열에서의 \ → 문자열 문법과 관련된 이스케이프
# 포매팅에서의 %% → % 포매팅 문법에서 % 자체를 출력하기 위한 규칙

# String formatting: specify the field width between % and s.
print("%10s" % "hi") # right direction
print("%-10s" % "hi") # left direction

print("%0.4f" % 3.42134234) # 소수점 4자리까지 표시
print("%10.4f" % 3.42134234) # 전체 길이 10, 소수점 4자리까지 표시
# (%0.4f): is a format specifier that indicates that the value to be inserted is a floating-point number with 4 digits after the decimal point.
# 소수점 앞은 위치를 나타내고, 소수점 뒤는 자릿수를 나타낸다.

# format() method: a more powerful way to format strings.
print("I eat {0} apples.".format(3))
print("I eat {0} apples.".format("five"))
# {}: placeholders for values to be inserted into the string.
# {0}: format()에 전달한 첫번째 인수의 위치(인덱스)를 의미함

print("I eat {0} apples. so I was sick for {1} days.".format(10, "three"))
# if you want to insert multiple values into a string, you can use the format() method
# 원래 파이썬에서는 인덱스를 표시할때 대괄호[]를 사용하지만, format()에서는 중괄호{}를 사용한다.
# (): 튜플을 만들거나 함수를 호출할때 사용한다.
# []: 리스트나 인덱스를 만들때 사용한다. 
# {}: 딕셔너리나 포맷팅을 만들때 사용한다.

print("I eat {number} apples. so I was sick for {day} days.".format(number=10, day="three"))
# if you want to insert values into a string using named placeholders, you can use the format() method with keyword arguments.

print("{0:<10}".format("hi")) # left direction
print("{0:>10}".format("hi")) # right direction
print("{0:^10}".format("hi")) # center direction

# % formatting: "% -10 s" % "hi"
# format() method: "{0 :< 10}". format("hi")
# f-string: f"{0 :< 10}" - recently added in Python 3.6, f-strings are a more concise way to format strings using expressions inside curly braces.

# print("%^10s" % "hi") 
# when you use the ^ symbol in % formatting, it will not work as expected. Instead, you can use the format() method or f-strings to achieve the same effect.

print("{0:=^10}".format("hi")) 
print(f"{0:=^10}")

print("{0:0.4f}".format(3.42134234)) 

F = 3.42134234
print(f"{F:0.4f}") #  f-string is allowed in Python 3.6 and later versions, so thay's why it doesn't work now

print("{{ and }}".format()) # if you want to include curly braces in the string, you can use double curly braces to escape them.
# {{ = %% 

# f-string: f"{value}" - recently added in Python 3.6, f-strings are a more concise way to format strings using expressions inside curly braces.
name = "홍길동"
age = 30
print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.")

d = {"name": "홍길동", "age": 30} # here {} is used to create a dictionary, which is a data structure that stores key-value pairs.
print(f"나의 이름은 {d['name']}입니다. 나이는 {d['age']}입니다.") # here {} is used to formatting the string, and [] is used to access the values in the dictionary using their keys.
# dictionary: {}
# access dictionary values using keys: []

print(f"{'hi':^10}") 
# when you use f-strings, you need to put f out of "" because python will recognize it as a string as well. 

print("{0:!^12}".format("python"))
print(f"{'python':!^12}")
# 안에 따옴표 있으면 다른 따옴표로 바꿔주어야함 왜냐하면 "{" 이렇게 인식하여 문법오류가 나기 때문이다. 

# String functions other than format()
# count(), find(), index(),find(), index(), join(), upper(), lower(), strip(), replace(), split()

a = "hobby"
print(a.count("b")) #count(): returns the number of occurrences of a substring in the string.
# a에 있는 문자열에서 b 를 세어보면 2개가 나온다. 그래서 2가 출력된다.

a =  "Python is the best choice"
print(a.find("b")) #find(): returns the index of the first occurrence of a substring in the string. If the substring is not found, it returns -1.
# 처음 발견되는 b의 위치를 반환한다. 만약 찾는 문자열이 없으면 -1을 반환한다.

a =  "Life is too short" 
a.index("t") #index(): returns the index of the first occurrence of a substring in the string. If the substring is not found, it raises a ValueError.
# 처음 발견되는 t의 위치를 반환한다. 만약 찾는 문자열이 없으면 ValueError를 발생시킨다.
# index()와 find()의 차이점은 찾는 문자열이 없을때 반환값이 다르다. find()는 -1을 반환하고, index()는 ValueError를 발생시킨다.

print(",".join("abcd")) #join(): returns a string that is the concatenation of the strings in the iterable, separated by the string on which join() is called.
# join(): 문자열을 합쳐주는 함수이다.

a = "hi"
print(a.upper()) #upper(): returns a copy of the string with all the characters converted to uppercase.

a = "HI"
print(a.lower()) #lower(): returns a copy of the string with all the characters converted to lowercase 

a = " hi "
print (a.strip()) #strip(): returns a copy of the string with leading and trailing whitespace removed.
# strip(): 문자열의 양쪽 공백을 제거하는 함수이다.
# lstrip(): returns a copy of the string with leading whitespace removed.
# rstrip(): returns a copy of the string with trailing whitespace removed.

a = "Life is too short"
print(a.replace("Life", "Your leg")) #replace(): returns a copy of the string
# with all occurrences of a substring replaced by another substring.
# replace(): 어떤 부분 문자열이 나타나는 모든 위치를 다른 부분 문자열로 변경한다.

a = "Life is too short"
print(a.split()) #split(): returns a list of the words in the string, using whitespace
# 여기서 split() 괄호 안의 기준으로 나눔 
# 만약 split(:) 이렇게 되어있다면 : 기준으로 나눔

a = "hi"
a.upper() # 이 경우 a.upper()를 실행하면 a의 값은 변하지 않는다. 왜냐하면 upper()는 새로운 문자열을 반환하기 때문이다. 따라서 a의 값은 여전히 "hi"이다.
a = a.upper() # 이 경우 a.upper()를 실행하면 a의 값이 변한다. 왜냐하면 upper()는 새로운 문자열을 반환하고, 그 값을 a에 다시 할당하기 때문이다. 따라서 a의 값은 이제 "HI"이다.
print(a)