a = int(input("type a side of the rectangle: "))
b = int(input("Type other side of the ractangle: "))

temp1 = b
temp2 = a
while temp1 > 0:
    if temp1 == b or temp1 == 1:
        while temp2 > 0:
            print("#", end="")
            temp2 = temp2 - 1
    else:
        while temp2 > 0:
            if temp2 == a or temp2 == 1:
                print("#", end="")
            else:
                print(" ", end="")
            temp2 = temp2 - 1
    temp1 = temp1 - 1
    temp2 = a
    print()

