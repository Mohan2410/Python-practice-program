angle1 = int(input("Enter 1st angle"))
angle2 = int(input("Enter 2nd angle"))
angle3 = int(input("Enter 3rd angle"))

if(angle1+angle2+angle3 == 180) and (angle1==angle2 or angle2==angle3 or angle3==angle1):
    print("It is triangle")
else:
    print("It is not triangle")
