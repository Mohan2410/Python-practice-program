# while loop
i = 1
while(i <= 5):
    print(i)
    i = i + 1
else:    #we can use the else block with the loop in python
    print("Else block is executed")
    print("Welcome")

# for loop

for i in range(1,6,1):
    print(i)
    if i == 4:
        break
    # end of loop
print("Welcome")



# Example
for i in range(1,9):
    print(i)
    if i == 5:
        break