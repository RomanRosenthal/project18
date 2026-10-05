n = int(input("enter a number of what you want to figure out the sum of: "))
sum = 0
for i in range(1, n + 1):
    sum = (sum + i)
print("the sum of first", n, "numbers is:", sum)
