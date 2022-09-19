from re import S


def square(s):
    #Complete the code given below
    # Replace the .... by your own code
    for i in range(s):
        if i%s==0 or i%s ==(s-1):
            print("* " * s)

        else:
            print("*", "  "* (s-3)," *")

print(square(3))
print(square(4))
print(square(6))
print(square(7))
print(square(8))
print(square(9))