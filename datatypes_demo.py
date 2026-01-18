age=20
height=5.9
name="ansiya"
is_student=True
print("Age",age,"Type",type(age))
print("Height",height,"Type",type(height))
print("Name",name,"Type",type(name))
print("Is Student",is_student,"Type",type(is_student))

print("\n----Arithmetic operations-----")
print("Addition",age+5)
print("Subtration",age-2)
print("Multiplication",age*2)
print("Division",age/2)

print("-------type casting----------")
num_str="100"
price_str="49.75"
num=int(num_str)
price=float(price_str)
print("Converted integer",num,"Type",type(num))
print("Converted float",price,"Type",type(price))

print("\n----handling invalid input---")
invalid_input="abd"
try:
    result=int(invalid_input)
except ValueError:
    print("invalid input!")

print("\n---string concatenation---")
print("my age is"+str(age))

print("\n----dynamic typing----")
value=10
print(value,"Type",type(value))
value="now i am a string"
print(value,"Type",type(value))
