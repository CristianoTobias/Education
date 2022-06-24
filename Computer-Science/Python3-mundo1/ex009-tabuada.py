num = int(input("Type a number for see your multiplication table: "))
print("*" * 10)
print("Using for")
for n in range(1, 11):
    print("{:2} * {} = {}".format(n, num, n * num))
print("*" * 10)

print("*" * 10)
print("using while")
count = 1
while count < 11:
    print(f"{count:2} * {num} = {count * num}")
    count += 1
print("*" * 10)
