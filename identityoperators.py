# We can use identity operators for address comparison.
# There are 2 identity operators are available
# 1) is 2) is not
#  r1 is r2 returns True if both r1 and r2 are pointing to the same object.
# r1 is not r2 returns True if both r1 and r2 are not pointing to the same object.
a=10
b=10
print(a is b)
#####another program####
a="sitesh"
b="sitesh"
print(id(a))
print(id(b))
print(a is b)

list1=["one","two","three"]
list2=["one","two","three"]
print(id(list1))
print(id(list2))
print(list1 is list2)
print(list1 is not list2)
print(list1 == list2)
##identity operators can be used for reference comparison but not for content comparison
# Membership Operators
# We can use Membership operators to check whether the given object present in the given collection. (It may be String, List, Set, Tuple OR Dict)  In  Returns True if the given object present in the specified Collection
# not in  Retruns True if the given object not present in the specified Collection
x="hello learning Python is very easy!!!"
print('h' in x)
print('d' in x)
print('d' not in x)
print('Python' in x)
# Eg: 1)
list1=["one","two","three","four"]
print("one" in list1)
print("two" in list1)
print("three" not in list1)
