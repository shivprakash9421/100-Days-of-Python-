a="23"
b="45"
a=int(a)
b=int(b)
sum=a+b
print(sum)

# EXCPLICIT TYPE CASTING(CONVERSION)

string = "15"
number = 7
string= int(string) #throws an error if the string is not a valid integer
sum= number + string
print("The Sum of both the numbers is: ", sum)


# IMPLICIT TYPE CASTING(CONVERSION)

d=1.9 
c=44
print(d+c)

# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.84
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))