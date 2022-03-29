

print("Q1")
print("Hello Glasgow!\n")
#--------------------------------------------
print("Q2")
def average(num1,num2):
    avg = (num1+num2)/2
    return avg
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
output = average(input1,input2)
print("The average of " + str(input1) + " and " + str(input2) + " is " + str(output))
print()
#------------------------------------------------
print("Q3")
module = "CSC1009"
if module == "CSC1006":
    print("Math 2")
elif module == "CSC1007":
    print("Operating systems")
elif module == "CSC1008":
    print("Data structures")
elif module == "CSC1009":
    print("Object-Oriented Programming")
print()
#-------------------------------------------------
print("Q4")
x = 102
while (x != 65):
    if x%2 != 0:
        print(x)
    x-=1
