def fizz_buzz(n):
    for num in range(1, n + 1):
        if num % 3 == 0:
            if num % 5 == 0:
                print("FizzBuzz")
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(str(num))


if __name__ == "__main__":
    fizz_buzz(100)
