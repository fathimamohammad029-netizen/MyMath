class MyMath:

    def calculate(self, operation, n):

        if operation == "sum":
            total = sum(range(1, n+1))
            print("Sum =", total)

        elif operation == "prime":
            count = 0
            num = 2
            while count < n:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    print(num, end=" ")
                    count += 1
                num += 1

        elif operation == "fibonacci":
            a, b = 0, 1
            for i in range(n):
                print(a, end=" ")
                a, b = b, a+b

        elif operation == "factorial":
            fact = 1
            for i in range(1, n+1):
                fact *= i
            print("Factorial =", fact)


math = MyMath()

print("1. Sum of first n natural numbers")
print("2. First n prime numbers")
print("3. Fibonacci series")
print("4. Factorial")

choice = int(input("Enter choice: "))
n = int(input("Enter value of n: "))

if choice == 1:
    math.calculate("sum", n)
elif choice == 2:
    math.calculate("prime", n)
elif choice == 3:
    math.calculate("fibonacci", n)
elif choice == 4:
    math.calculate("factorial", n)
