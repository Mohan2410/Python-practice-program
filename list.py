# Example: 01
mylist = [10,20,30,40,50]

mylist[0] = 20

print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])

print("mylist = ",mylist)

# Example: 02
a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))

mylist = [1,2,3,4,5,6]

if(a in mylist):
    print("a is available in the list")
else:
    print("a is not available in the list")
    if(b in mylist):
        print("b is available in the list")
    else:
        print("b is not available in the list")