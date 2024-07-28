# print the following output
# 12345
# 12345
# 12345
# 12345
for j in range(1,5):
    for i in range(1,6):
        print(i,end="")
    print(j)

# print the following output
# ABCDE
# ABCDE
# ABCDE
# ABCDE
# ABCDE
for j in range(1,6):
    for i in range(65,70):
        print(chr(i),end="")
    print()

# print the following output
# 1
# 12
# 123
# 1234
# 12345
for j in range(1,6):
    for i in range(1,j+1):
        print(i,end="")
    print()

# print the following output
# A
# AB
# ABC
# ABCD
# ABCDE
for j in range(65,70):
    for i in range(65,j+1):
        print(chr(i),end="");
    print()