t1 = ()
t2 = (1,) # A trailing comma is required for a single-element tuple. Otherwise, Python treats it as an integer inside parentheses.
# Why (1) is an integer, not a tuple: Python interprets these parentheses as mathematical operators (operator precedence) rather than a tuple definition.
t3 = (1,2,3)
t4 = 1,2,3 # Parentheses can be omitted when defining a tuple.
t5 = ("a", "b", ("ab", "cd")) 
# Difference between Tuple and List: Tuples are immutable, while lists are mutable.
# Unlike lists, elements inside a tuple cannot be deleted or modified. 

t1 = (1,2,"a","b")
print(t1[1]) # Tuples support indexing.
print(t1[0:2])

t1 = (1,2,"a","b")
t2 = (3,4)
t3 = t1 + t2 
print(t3) 
# Note: The original tuple values did not change; instead, a brand new tuple (t3) was created.

t1 = (1,2,"a","b")
t2 = t1 * 2
print(t2) # Similarly, multiplication creates a brand new tuple.

t1 = (1,2,"a","b")
print(len(t1))
# Just like lists, you can get the length of a tuple using the len() function.

t1 = (1,2,3)
t2 = (4,)
t3 = t1 + t2
print(t3)