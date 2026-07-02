# Boolean Type: A data type that represents True or False.
# Note: 'True' and 'False' are Python keywords and must always start with a capital letter. (Keyword: A reserved word pre-defined for syntax operation)
# type(): A function that returns the data type of a given value.

a = True
b = False
print(type(a))
print(type(b))

print(1 == 1)
print(2 > 1)
print(2 < 1)

# Truth Value of Data Types: Strings, lists, tuples, dictionaries, etc., evaluate to False if empty, and True if not empty.

a = [1,2,3,4]
while a: 
    print(a.pop()) # The while loop checks if list 'a' evaluates to True or False; it continues executing pop() as long as 'a' is True (not empty).
if []: # Python's evaluation: Prints "참" if [] is True, and prints "거짓" if [] is False.
    print("참") 
else: 
    print("거짓")
# Conclusion: Since the list [] is empty, it evaluates to False and prints "거짓".

a = [1,2,3]
if a: 
    print("True")
else: 
    print("False")

print(bool("python"))
print(bool([]))
# bool(): You can use this function to easily check whether a value evaluates to True or False.