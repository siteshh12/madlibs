# # Operator Precedence
# ()  Parenthesis
#  **  Exponential Operator
# ~, -  Bitwise Complement Operator, Unary Minus Operator
# *, /, %, //  Multiplication, Division, Modulo, Floor Division
#  +, -  Addition, Subtraction
# <<, >>  Left and Right Shift
# &  Bitwise And
# ^  Bitwise X-OR
# |  Bitwise OR
#  >, >=, <, <=, ==, !=  Relational OR Comparison Operators
# =, +=, -=, *=...  Assignment Operators
# is , is not  Identity Operators
# in , not in  Membership operators
# not  Logical not
# and  Logical and
# or  Logical or
a=30
b=20
c=10
d=5
print((a+b)*c/d)
print((a+b)*(c/d))
print(a+(b*c)/d)
print((a+b)*c)