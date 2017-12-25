var = input("enter a value :")
var2 = input("enter another value to divide :")
""""
Starting Try
"""
try:
    result = var/var2
    print result
except ZeroDivisionError:
    print("zero division error!")
finally:
    print("end of the program")
