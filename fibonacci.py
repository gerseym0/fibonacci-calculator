def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def main():
    n = int(input("Введіть число для розрахунку n-го числа Фібоначчі: "))
    print(f"{n}-е число Фібоначчі: {fibonacci(n)}")

if __name__ == "__main__":
    main()
