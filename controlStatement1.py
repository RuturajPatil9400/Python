num = 10

if num > 0:
    print("The number is positive.")


if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

if num < 0:
    print("The number is negative.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is positive.")


if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is not positive.")
