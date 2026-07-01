a = [] # This is an empty list
b = [1, 2, 3, 4, 5] # This is a list of integers
c = ['a', 'b', 'c', 'd', 'e'] # This is a list of strings
d = [1, 'a', 2, 'b', 3, 'c'] # This is a list of mixed data types
e = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # This is a list of lists
# []: list 

a = [1,2,3]
print(a[0]) # how to index a list: using the index number inside square brackets
print(a[1]+a[2]) # you can also perform operations on the indexed values

a = [1,2,3,[4,5,6]]
print(a[3]) # This will print the sublist [4,5,6]
print(a[3][0]) # This will print the first element of the sublist, which is 4
# 리스트를 다중으로 사용하는 것은 혼란스럽기 때문에 권장되지 않습니다. 

# list slicing is same to string slicing.
a = [1,2,3,4,5]
print(a[0:3]) # this will print the first three elements of the list: [1, 2, 3]
a = "12345"
print(a[0:3]) # this will print the first three characters of the string: 123

a = [1,2,3,4,5]
print(a[1:3])

# List operations
a = [1,2,3]
b = [4,5,6]
print(a + b) # This will concatenate the two lists: [1, 2, 3, 4, 5, 6]
a = [1,2,3]
print(a * 3) # This will repeat the list three times: [1, 2, 3, 1, 2, 3, 1, 2, 3]   

# List methods 

# how to get the length of a list
a = [1,2,3] 
print(len(a)) # This will print the length of the list: 3

# how to change the value of a list element
a = [1,2,3]
a[1] = 4 # This will change the second element of the list to 4
print(a) # This will print the modified list: [1, 4, 3

# how to delete an element from a list
a = [1,2,3]
del a[1] # This will delete the second element of the list
print(a) # This will print the modified list: [1, 3]

# how to add an element to the end of a list
a = [1,2,3]
a.append(4) # This will add the element 4 to the end of the list(리스트 마지막에 추가됨)
print(a) # This will print the modified list: [1, 2, 3, 4]

# how to sort elements in a list
a = [1,4,3,2]
a = a.sort() # Modifies the original data directly
print(a) # 그래서 a의 값은 none으로 출력된다. 

a = [1,4,3,2]
print(sorted(a)) # Keeps the original data as is, and returns a new sorted list.
print(a)

a = [1,4,3,2]
a.sort()
print(a)

# how to reverse list
a = ["a", "c", "b"]
a.reverse()
print(a)

# how to index
a = [1,2,3]
print(a.index(1)) 

# how to insert 
a = [1,2,3]
a.insert(0,4) # replace(): Used for strings to swap an existing substring with a new one.
print(a) # insert(index, element): inserts 'element' at the specified 'index'

# how to remove
a = [1,2,3,1,2,3]
a.remove(3) # Removes only the first occurrence of 3
a.remove(3) # Must call it twice to remove all 3s
print(a)

# how to pop an element out in a list
a = [1,2,3]
a.pop(2) # The '2' inside the parentheses represents the index number.
print(a) # pop(): removes and returns the item at that position.

# how to count specific element in a list
a = [1,2,3,1] 
print(a.count(1)) # Pass the element you want to count inside the parentheses.
# how to add a list to an original list
a = [1,2,3]
b = [4, 5, 6]
a.extend(b) # Extends list 'a' by adding all elements from list 'b'.
print(a)